"""Build the Nov 16–22 noon carousel batch. argv[1] = urls json (filename -> signed url)."""
import json, sys

IG, TT = "6aa73d44ea19ca0bde3a2b2f", "6aa73d68ea19ca0bde3a2bb5"
LINKS = ("🌐: https://fridgesmartapp.com\n\n📱: https://apps.apple.com/app/id6755790933\n\n"
         "🤖: https://play.google.com/store/apps/details?id=com.minafakhri.fridgesmart")
BIO = "🔗 Download links in bio"
U = json.load(open(sys.argv[1]))
OLD = json.load(open("posts/nov10-15-urls.json"))  # Nov 10/11 carousels (TikTok reuse)

def cap(body, tags, ig=False): return f"{body}\n\n{BIO if ig else LINKS}\n\n{tags}"
def slides(prefix, n, alt, src=None):
    src = src or U
    return [{"image": {"url": src[f"{prefix}-{i:02d}.jpg"], "metadata": {"altText": f"{alt}, slide {i}"}}} for i in range(1, n + 1)]

C = {  # day: (prefix, n, alt, body, tags, tt_title, on_ig, on_tt)
 "16": ("nov16", 7, "Is your fridge cold enough", "Is your fridge cold enough? 🌡️ Check it this week, before the turkey moves in. Source: FoodSafety.gov + USDA.",
        "#FoodSafety #Thanksgiving #KitchenTips #FridgeSmart", "Is your fridge cold enough?", True, False),
 "17": ("nov17", 7, "5 turkey myths", "5 turkey myths your family still believes 🦃 Send this to whoever's cooking Thursday. Source: USDA.",
        "#Thanksgiving #FoodSafety #TurkeyTips #FridgeSmart", "5 turkey myths your family still believes 🦃", True, True),
 "18": ("nov18", 6, "Monthly vs Founder's Lifetime math", "$4.99 a month adds up 😩 Founder's Lifetime: $99.99 once, every FridgeSmart+ benefit for life. Ends Cyber Monday, Nov 30 at 11:59 PM ET. Get it at fridgesmartapp.com",
        "#FridgeSmart #LifetimeDeal #CyberMonday", "Stop paying every month: Founder's Lifetime $99.99", True, True),
 "19": ("nov19", 4, "Thanksgiving fridge prep checklist", "Thanksgiving fridge prep checklist 📋 Save it and do it this weekend. Thaw times from the USDA.",
        "#Thanksgiving #FridgeOrganization #KitchenTips #FridgeSmart", "Thanksgiving fridge prep checklist", True, True),
 "20": ("nov20", 4, "Founder's Lifetime: 10 days left", "10 days left ⏳ Founder's Lifetime: $99.99 once, every FridgeSmart+ benefit for life. Ends Cyber Monday, Nov 30 at 11:59 PM ET. Get it at fridgesmartapp.com",
        "#FridgeSmart #LifetimeDeal #CyberMonday", "Founder's Lifetime: 10 days left ⏳", True, True),
 "21": ("nov21", 7, "Thanksgiving leftovers quiz", "How long do Thanksgiving leftovers actually last? 🦃 Guess first, then swipe. How many did you get? Source: USDA + FoodSafety.gov.",
        "#Thanksgiving #Leftovers #FoodSafety #FridgeSmart", "How long do Thanksgiving leftovers last?", True, True),
 "22": ("nov22", 7, "5 meals from leftover turkey", "5 meals from leftover turkey 🦃 Save this for Friday.",
        "#Thanksgiving #Leftovers #EasyDinners #FridgeSmart", "5 meals from leftover turkey", True, False),
}
posts = []
for d, (p, n, alt, body, tags, tt, on_ig, on_tt) in sorted(C.items()):
    due = f"2026-11-{d}T12:00:00-05:00"
    if on_ig:
        posts.append({"day": d, "channelId": IG, "dueAt": due, "text": cap(body, tags, True), "assets": slides(p, n, alt),
                      "metadata": {"instagram": {"type": "post", "shouldShareToFeed": True}}})
    if on_tt:
        posts.append({"day": d, "channelId": TT, "dueAt": due, "text": cap(body, tags), "assets": slides(p, n, alt),
                      "metadata": {"tiktok": {"title": tt}}})
# TikTok reuse of Nov 10/11 carousels that never went to TikTok
posts.append({"day": "16", "channelId": TT, "dueAt": "2026-11-16T12:00:00-05:00",
              "text": cap("Your fridge has zones, and most of us use them wrong 😬 Save this and fix yours tonight.", "#FridgeOrganization #KitchenTips #FoodSafety #FridgeSmart"),
              "assets": slides("nov10", 8, "Fridge zones guide", OLD), "metadata": {"tiktok": {"title": "Your fridge has zones"}}})
posts.append({"day": "22", "channelId": TT, "dueAt": "2026-11-22T12:00:00-05:00",
              "text": cap("1 rotisserie chicken = 5 dinners 🍗 Save this for your next grocery run.", "#MealPrep #EasyDinners #FoodWaste #FridgeSmart"),
              "assets": slides("nov11", 8, "1 rotisserie chicken, 5 dinners", OLD), "metadata": {"tiktok": {"title": "1 rotisserie chicken, 5 dinners"}}})
posts.sort(key=lambda x: (x["dueAt"], x["channelId"]))
json.dump(posts, open("posts/batch-nov16-22-noon.json", "w"), ensure_ascii=False, indent=1)
print(len(posts), [(x["day"], x["channelId"][-4:]) for x in posts])
