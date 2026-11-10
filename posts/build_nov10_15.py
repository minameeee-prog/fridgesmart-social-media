"""Build the Nov 10–15 Buffer batch from the imported signed URLs (urls json: filename -> url)."""
import json, sys

IG, TT, YT = "6aa73d44ea19ca0bde3a2b2f", "6aa73d68ea19ca0bde3a2bb5", "6aa73dc5ea19ca0bde3a2cfc"
LINKS = ("🌐: https://fridgesmartapp.com\n\n📱: https://apps.apple.com/app/id6755790933\n\n"
         "🤖: https://play.google.com/store/apps/details?id=com.minafakhri.fridgesmart")
BIO = "🔗 Download links in bio"
U = json.load(open(sys.argv[1]))

def cap(body, tags, ig=False):
    return f"{body}\n\n{BIO if ig else LINKS}\n\n{tags}"

def slides(prefix, n, alt):
    return [{"image": {"url": U[f"{prefix}-{i:02d}.jpg"], "metadata": {"altText": f"{alt}, slide {i}"}}} for i in range(1, n + 1)]

def vid(name, off):
    return [{"video": {"url": U[name], "metadata": {"thumbnailOffset": off}}}]

CAROUSELS = {  # day: (prefix, n, alt, body, tags, tiktok_title, tiktok?)
 "10": ("nov10", 8, "Fridge zones guide", "Your fridge has zones, and most of us use them wrong 😬 Save this and fix yours tonight.",
        "#FridgeOrganization #KitchenTips #FoodSafety #FridgeSmart", "Your fridge has zones", False),
 "11": ("nov11", 8, "1 rotisserie chicken, 5 dinners", "1 rotisserie chicken = 5 dinners 🍗 Save this for your next grocery run.",
        "#MealPrep #EasyDinners #FoodWaste #FridgeSmart", "1 rotisserie chicken, 5 dinners", False),
 "12": ("nov12", 6, "How long food lasts in the fridge", "How long food really lasts in your fridge 🥩🥚 Screenshot this one. Source: FoodSafety.gov.",
        "#FoodSafety #KitchenTips #FoodWaste #FridgeSmart", "How long food really lasts in your fridge", True),
 "13": ("nov13", 7, "Shared fridge rules", "Shared fridge rules that end the fights 🥛👀 Tag the person who keeps eating your leftovers.",
        "#FamilyLife #Roommates #FoodWaste #FridgeSmart", "Shared fridge rules that end the fights", True),
 "14": ("nov14", 7, "5 freezer myths", "5 freezer myths you probably believe 🧊 How many did you get right? Source: USDA.",
        "#FoodSafety #FreezerTips #KitchenTips #FridgeSmart", "5 freezer myths you probably believe", True),
 "15": ("nov15", 7, "5 meals from leftovers", "Use-it-up Sunday 🍳 5 meals from whatever's left in your fridge.",
        "#SundayReset #FoodWaste #EasyDinners #FridgeSmart", "5 meals from whatever's left", False),
}
VIDEOS = {  # day: (file, offset, body, tags, title, tiktok?)
 "10": ("quick-scan-story-video.mp4", 16150, "“When did we open this?” 🤨 Quick Scan it once and FridgeSmart remembers the date for you. Real app, sped up.",
        "#FridgeSmart #KitchenHacks #FoodWaste #Relatable", "“When did we open this?” Scan it once 📸", True),
 "11": ("chef-lumi-nothing-to-eat-video.mp4", 14250, "Full fridge. “There's nothing to eat.” 😩 Chef Lumi turns what you already have into dinner.",
        "#WhatsForDinner #EasyDinners #FoodWaste #FridgeSmart", "Full fridge, “nothing to eat” 😩 Ask Chef Lumi", True),
 "12": ("lifetime-monthly-story-video.mp4", 16250, "36 payments of $4.99 = $179.64 😩 Or pay once: Founder's Lifetime is $99.99, one time, every FridgeSmart+ benefit. Ends Cyber Monday, Nov 30 at 11:59 PM ET. Get it at fridgesmartapp.com",
        "#FridgeSmart #LifetimeDeal #CyberMonday", "Stop paying every month: Founder's Lifetime $99.99", True),
 "13": ("who-ate-my-yogurt-video.mp4", 14650, "Who ate my yogurt?? 🥄👀 With Family Fridge, everyone sees the same fridge.",
        "#FamilyLife #Relatable #FoodWaste #FridgeSmart", "Who ate my yogurt?? 👀", False),
 "14": ("habits-to-quit-video.mp4", 20250, "4 kitchen habits the USDA says to quit 😬 How many do you do? Be honest.",
        "#FoodSafety #KitchenTips #CookingTips #FridgeSmart", "4 kitchen habits the USDA says to quit 😬", True),
 "15": ("lifetime-15-days-video.mp4", 12750, "15 days left ⏳ Founder's Lifetime: every FridgeSmart+ benefit for $99.99, once. Ends Cyber Monday, Nov 30 at 11:59 PM ET. Get it at fridgesmartapp.com",
        "#FridgeSmart #LifetimeDeal #CyberMonday", "Founder's Lifetime: 15 days left ⏳", True),
}
posts = []
for d in sorted(CAROUSELS):
    p, n, alt, body, tags, tt_title, on_tt = CAROUSELS[d]
    due = f"2026-11-{d}T12:00:00-05:00"
    posts.append({"day": d, "slot": "noon", "channelId": IG, "dueAt": due, "text": cap(body, tags, ig=True), "assets": slides(p, n, alt),
                  "metadata": {"instagram": {"type": "post", "shouldShareToFeed": True}}})
    if on_tt:
        posts.append({"day": d, "slot": "noon", "channelId": TT, "dueAt": due, "text": cap(body, tags), "assets": slides(p, n, alt),
                      "metadata": {"tiktok": {"title": tt_title}}})
for d in sorted(VIDEOS):
    f, off, body, tags, title, on_tt = VIDEOS[d]
    due = f"2026-11-{d}T19:30:00-05:00"
    posts.append({"day": d, "slot": "eve", "channelId": IG, "dueAt": due, "text": cap(body, tags, ig=True), "assets": vid(f, off),
                  "metadata": {"instagram": {"type": "reel", "shouldShareToFeed": True}}})
    if on_tt:
        posts.append({"day": d, "slot": "eve", "channelId": TT, "dueAt": due, "text": cap(body, tags), "assets": vid(f, off),
                      "metadata": {"tiktok": {"title": title}}})
    posts.append({"day": d, "slot": "eve", "channelId": YT, "dueAt": due, "text": cap(body, tags + " #Shorts"), "assets": vid(f, off),
                  "metadata": {"youtube": {"title": title, "categoryId": "26"}}})
# TikTok retries of last week's failed posts (never reached TikTok)
R = {"nov8": slides("nov8", 4, "Sunday fridge reset checklist")}
posts.append({"day": "13", "slot": "eve", "channelId": TT, "dueAt": "2026-11-13T19:30:00-05:00", "retry": True,
              "text": cap("Does this go bad? 🤔 Play along. How many did you get right?", "#FoodSafety #FoodWaste #KitchenTips #FridgeSmart"),
              "assets": vid("does-it-go-bad-video.mp4", 21250), "metadata": {"tiktok": {"title": "Does this go bad? Quiz"}}})
posts.append({"day": "15", "slot": "noon", "channelId": TT, "dueAt": "2026-11-15T12:00:00-05:00", "retry": True,
              "text": cap("The 10-minute Sunday fridge reset 🧽 Save this and do it tonight.", "#SundayReset #FridgeOrganization #FoodWaste #FridgeSmart"),
              "assets": R["nov8"], "metadata": {"tiktok": {"title": "The 10-minute Sunday fridge reset"}}})
json.dump(posts, open("posts/batch-nov10-15.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter
print(len(posts), Counter((p["channelId"][-4:], p["day"]) for p in posts))
