"""IG + YouTube noon reels Nov 18-22 (replacing IG carousels) + Meta receipt video Nov 17 7:30 PM.
argv[1] = urls json (repo path -> signed url). Writes batch-reels-nov17-22.json."""
import json, sys, subprocess
IG, TT, YT = "6aa73d44ea19ca0bde3a2b2f", "6aa73d68ea19ca0bde3a2bb5", "6aa73dc5ea19ca0bde3a2cfc"
LINKS = ("🌐: https://fridgesmartapp.com\n\n📱: https://apps.apple.com/app/id6755790933\n\n"
         "🤖: https://play.google.com/store/apps/details?id=com.minafakhri.fridgesmart")
BIO = "🔗 Download links in bio"
U = json.load(open(sys.argv[1]))

def dur_ms(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path], capture_output=True, text=True).stdout
    return int(float(out) * 1000)

V = [  # day, time, file, body, tags, title, ai, channels
 ("17", "19:30", "2026-11-17/meta-receipt.mp4",
  "30–40% of America's food supply gets wasted 😳 Not just milk. Everything. Scan your receipt and FridgeSmart gives every item an expiry date. (Source: USDA)",
  "#FoodWaste #GroceryHaul #SaveMoney #FridgeSmart", "Scan your receipt. Waste less. 🧾", True, (IG, TT, YT)),
 ("18", "12:00", "2026-11-18/reel-thanksgiving-prep.mp4",
  "Thanksgiving fridge prep checklist 📋 Save it and do it before Thursday. Thaw times from the USDA. Comment TURKEY if your bird is already thawing 🦃",
  "#Thanksgiving #FridgeOrganization #KitchenTips #FridgeSmart", "Thanksgiving fridge prep checklist 📋", False, (IG, YT)),
 ("19", "12:00", "2026-11-19/reel-turkey-myths.mp4",
  "5 turkey myths your family still believes 🦃 How many did you believe? Send this to whoever's cooking Thursday. Source: USDA.",
  "#Thanksgiving #FoodSafety #TurkeyTips #FridgeSmart", "5 turkey myths your family still believes 🦃", False, (IG, YT)),
 ("20", "12:00", "2026-11-20/reel-lifetime-10-days.mp4",
  "10 days left ⏳ Founder's Lifetime: $99.99 once, every FridgeSmart+ benefit for life. Ends Cyber Monday, Nov 30 at 11:59 PM ET. Get it at fridgesmartapp.com",
  "#FridgeSmart #LifetimeDeal #CyberMonday", "Founder's Lifetime: 10 days left ⏳", False, (IG, YT)),
 ("21", "12:00", "2026-11-21/reel-leftovers-quiz.mp4",
  "How long do Thanksgiving leftovers actually last? 🤔 Guess before the answer pops up. How many did you get? Source: USDA + FoodSafety.gov.",
  "#Thanksgiving #Leftovers #FoodSafety #FridgeSmart", "How long do Thanksgiving leftovers last? 🤔", False, (IG, YT)),
 ("22", "12:00", "2026-11-22/reel-leftover-turkey-meals.mp4",
  "5 meals from leftover turkey 🦃 Save this for Friday. Which one are you making?",
  "#Thanksgiving #Leftovers #EasyDinners #FridgeSmart", "5 meals from leftover turkey 🦃", False, (IG, YT)),
]
posts = []
for d, hm, f, body, tags, title, ai, chans in V:
    off = dur_ms(f) - 250; due = f"2026-11-{d}T{hm}:00-05:00"
    asset = [{"video": {"url": U[f], "metadata": {"thumbnailOffset": off}}}]
    for ch in chans:
        if ch == IG:
            text, meta = f"{body}\n\n{BIO}\n\n{tags}", {"instagram": {"type": "reel", "shouldShareToFeed": True, "isAiGenerated": ai}}
        elif ch == TT:
            text, meta = f"{body}\n\n{LINKS}\n\n{tags}", {"tiktok": {"title": title, "isAiGenerated": ai}}
        else:
            text, meta = f"{body}\n\n{LINKS}\n\n{tags} #Shorts", {"youtube": {"title": title, "categoryId": "26", "isAiGenerated": ai}}
        posts.append({"day": d, "channelId": ch, "dueAt": due, "text": text, "assets": asset, "metadata": meta})
json.dump(posts, open("batch-reels-nov17-22.json", "w"), ensure_ascii=False, indent=1)
print(len(posts), [(p["day"], p["channelId"][-4:]) for p in posts])
