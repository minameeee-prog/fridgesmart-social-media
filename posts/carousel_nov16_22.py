"""Nov 16–22 noon carousels (1080x1350) on the shared carousel base."""
import sys
from carousel import brand, render
from carousel_nov5_8 import EXTRA, cta, cover

SCAN = "/home/claude/fridgesmart-social-media/assets/app-demo/still-scanning.png"
CONFIRM = "/home/claude/fridgesmart-social-media/assets/app-demo/still-confirm-items.png"

def src(t): return f"<div class='src'>{t}</div>"
def deco(e): return f"<div class='emoji' style='position:absolute;left:72px;bottom:150px;font-size:120px;letter-spacing:14px;white-space:nowrap'>{e}</div>"

def life_cta(total, kick, title):
    return brand(total, total) + EXTRA + f"""
      <div style="position:absolute;left:72px;right:72px;top:250px">
        <div class="kick">{kick}</div>
        <h1 style="font-size:104px;margin-top:20px">{title}</h1>
        <div style="margin-top:40px;font-size:36px;color:#cfe6e4;line-height:1.35;max-width:880px">Founder's Lifetime: <b style="color:#fff">$99.99, one time.</b> Ends Cyber Monday, Nov 30 at 11:59 PM ET.</div>
        <div style="margin-top:56px"><span class="cta">Get Lifetime</span></div>
        <div style="margin-top:26px;font-size:30px;color:#cfe6e4;font-weight:600">fridgesmartapp.com</div>
      </div>
      <div class='lumi' style='width:280px;height:280px;right:60px;bottom:80px'><img src='chef-lumi-avatar.png'></div>"""

# Mon 16 (IG): fridge temperature
def nov16():
    pts = [("40°F", "Fridge: 40°F or below", "That's the line for keeping perishable food safe.", "🧊"),
           ("0°F", "Freezer: 0°F or below", "Frozen food kept at 0°F stays safe. Quality is what fades.", "❄️"),
           ("Check", "The dial isn't a thermometer", "“Colder” on the dial doesn't tell you the temperature. A cheap appliance thermometer does.", "🌡️"),
           ("20 min", "Above 40°F, bacteria move fast", "In the 40–140°F danger zone, bacteria can double in as little as 20 minutes.", "🦠"),
           ("2 hrs", "Leftovers in within 2 hours", "Big holiday meal? Split leftovers into shallow containers so they cool fast.", "🥡")]
    total = len(pts) + 2; s = []
    s.append(cover(total, "BEFORE THANKSGIVING", "Is your fridge <em>cold enough?</em>",
        "Check it this week, before the turkey moves in.", deco("🌡️🧊🦃")))
    for k, (big, head, body, e) in enumerate(pts, 1):
        s.append(brand(total, k + 1) + EXTRA + f"""
          <div style="position:absolute;left:72px;right:72px;top:200px">
            <div class="num" style="font-size:{170 if len(big) < 6 else 140}px">{big}</div>
            <h1 style="font-size:84px;margin-top:20px;max-width:900px">{head}</h1></div>
          <div class="card right" style="position:absolute;left:72px;right:72px;top:780px;font-size:42px">{body}</div>
          <div class="emoji" style="position:absolute;right:80px;top:190px;font-size:150px">{e}</div>""" +
          src("Sources: FoodSafety.gov, USDA FSIS"))
    s.append(cta(total, "KEEP TABS ON IT ALL", "Know what's in there <em>and when it expires.</em>",
        "Snap your fridge once. FridgeSmart dates every item and reminds you before it goes bad.", SCAN))
    render(s, "nov16")

# Tue 17 (IG + TT): turkey myths
def nov17():
    myths = [("Wash the turkey before it goes in the oven.", "Don't. Washing raw poultry doesn't make it cleaner. It splashes bacteria around your sink.", "🚰"),
             ("Thawing on the counter is fine.", "Thaw it in the fridge (24 hrs per 4–5 lbs), in cold water (30 min per lb) or in the microwave.", "🕒"),
             ("If the juices run clear, it's done.", "You can't tell by color. It's done at 165°F in the thigh, the wing and the thickest part of the breast.", "🌡️"),
             ("Stuff it the night before to save time.", "Don't stuff it ahead. USDA suggests cooking stuffing in a separate dish.", "🥖"),
             ("Leftovers can wait until after dessert.", "Get them in the fridge within 2 hours of cooking.", "🥧")]
    total = len(myths) + 2; s = []
    s.append(cover(total, "THANKSGIVING MYTH BUSTERS", "5 turkey myths <em>your family still believes</em>",
        "Straight from the USDA. Send this to whoever's cooking.", deco("🦃🥧🌡️")))
    for k, (m, f, e) in enumerate(myths, 1):
        s.append(brand(total, k + 1) + EXTRA + f"""
          <div style="position:absolute;left:72px;right:72px;top:200px"><div class="num">{k:02d}</div></div>
          <div class="card wrong" style="position:absolute;left:72px;right:72px;top:420px;font-size:50px;font-family:Poppins;font-weight:700"><b>✕ MYTH</b>“{m}”</div>
          <div class="card right" style="position:absolute;left:72px;right:72px;top:810px;font-size:40px"><b>✓ FACT</b>{f}</div>
          <div class="emoji" style="position:absolute;right:80px;top:180px;font-size:150px">{e}</div>""" +
          src("Source: USDA FSIS Thanksgiving food safety"))
    s.append(cta(total, "AFTER THE FEAST", "Track the leftovers <em>so nothing gets wasted.</em>",
        "FridgeSmart dates every container and reminds you before it's too late.", CONFIRM))
    render(s, "nov17")

# Wed 18 (IG + TT): Lifetime math
def nov18():
    steps = [("$4.99", "a month adds up", "That's $59.88 every single year.", "💳"),
             ("$119.76", "after 2 years of monthly", "And it keeps going, every month you keep it.", "💸"),
             ("$99.99", "once. That's it.", "Founder's Lifetime: every FridgeSmart+ benefit, for life. No renewals.", "✨"),
             ("&lt;2 yrs", "and it's paid for itself", "Compared with paying monthly, Lifetime is ahead within 21 months.", "📈")]
    total = len(steps) + 2; s = []
    s.append(cover(total, "FOUNDER'S LIFETIME", "Stop paying for FridgeSmart+ <em>every month</em>",
        "Do the math with us. Swipe →", deco("🧮💳✨")))
    for k, (big, line, body, e) in enumerate(steps, 1):
        s.append(brand(total, k + 1) + EXTRA + f"""
          <div style="position:absolute;left:72px;right:72px;top:220px">
            <div class="num" style="font-size:180px">{big}</div>
            <h1 style="font-size:80px;margin-top:20px">{line}</h1></div>
          <div class="card right" style="position:absolute;left:72px;right:72px;top:800px;font-size:42px">{body}</div>
          <div class="emoji" style="position:absolute;right:80px;top:200px;font-size:140px">{e}</div>""")
    s.append(life_cta(total, "ENDS CYBER MONDAY", "Pay once. <em>Keep it for life.</em>"))
    render(s, "nov18")

# Thu 19 (IG + TT): Thanksgiving fridge prep checklist
def nov19():
    items = ["Toss anything expired or forgotten in the back.",
             "Start thawing the turkey in the fridge: 24 hrs per 4–5 lbs. A 15-lb bird needs 3–4 days.",
             "Clear the bottom shelf and set the turkey on a tray so juices can't drip.",
             "Check the fridge is at 40°F or below.",
             "Stock up on shallow containers for leftovers.",
             "Plan the leftovers: eat within 4 days or freeze."]
    total = 4; s = []
    s.append(cover(total, "SAVE THIS", "Thanksgiving fridge prep <em>checklist</em>",
        "Do it this weekend. Thank yourself on Thursday.", deco("🦃📋🧊")))
    for part, chunk in enumerate([items[:3], items[3:]], 2):
        rows = "".join(f"<div class='check'><i>✓</i><div>{t}</div></div>" for t in chunk)
        s.append(brand(total, part) + EXTRA + f"""
          <div style="position:absolute;left:72px;right:72px;top:190px">
            <div class="kick">{'THIS WEEKEND' if part == 2 else 'BEFORE THURSDAY'}</div>
            <h1 style="font-size:84px;margin:14px 0 40px">{'Make room' if part == 2 else 'Get ready for leftovers'}</h1>{rows}</div>""" +
          src("Thawing, temperature and leftover times: USDA FSIS, FoodSafety.gov"))
    s.append(cta(total, "CHECK #1, DONE FOR YOU", "See everything <em>in your fridge.</em>",
        "Snap it once. FridgeSmart lists every item with its date.", SCAN))
    render(s, "nov19")

# Fri 20 (IG + TT): Lifetime countdown
def nov20():
    total = 4; s = []
    s.append(brand(total, 1) + EXTRA + """
      <div style="position:absolute;left:72px;right:72px;top:230px">
        <div class="kick">FOUNDER'S LIFETIME</div>
        <div class="num" style="font-size:300px;margin-top:10px">10</div>
        <h1 style="font-size:120px;margin-top:-10px">days <em>left</em></h1>
        <div style="margin-top:40px;font-size:36px;color:#cfe6e4;line-height:1.35;max-width:820px">Then it's gone. Swipe for the details.</div>
      </div><div class="emoji" style="position:absolute;right:90px;top:300px;font-size:200px">⏳</div><div class="swipe">Swipe →</div>""")
    for k, (big, line, e) in enumerate([("$99.99", "One payment. No renewals. Ever.", "💳"),
                                         ("For life", "Every FridgeSmart+ benefit, forever.", "✨")], 2):
        s.append(brand(total, k) + EXTRA + f"""
          <div style="position:absolute;left:72px;right:72px;top:260px">
            <div class="num" style="font-size:200px">{big}</div>
            <h1 style="font-size:92px;margin-top:30px">{line}</h1></div>
          <div class="emoji" style="position:absolute;left:0;right:0;top:900px;text-align:center;font-size:220px">{e}</div>""")
    s.append(life_cta(total, "ENDS CYBER MONDAY, NOV 30", "Don't miss <em>the founder price.</em>"))
    render(s, "nov20")

# Sat 21 (IG + TT): leftovers quiz
def nov21():
    qs = [("Cooked turkey in the fridge?", "3–4 days", "Or “until the Monday after Thanksgiving.”", "🦃"),
          ("Cooked turkey in the freezer?", "2–6 months", "For best quality. Frozen at 0°F, it stays safe longer.", "❄️"),
          ("On the table before it goes in the fridge?", "2 hours", "Just 1 hour if it's over 90°F.", "⏱️"),
          ("Thawed raw turkey in the fridge?", "1–2 days", "Then cook it.", "🥶"),
          ("Leftover turkey soup in the fridge?", "3–4 days", "Or 2–3 months in the freezer.", "🍲")]
    total = len(qs) + 2; s = []
    s.append(cover(total, "QUIZ", "How long do Thanksgiving leftovers <em>actually last?</em>",
        "Guess before you swipe. Count how many you get right.", deco("🦃🥡🤔")))
    for k, (q, a, note, e) in enumerate(qs, 1):
        s.append(brand(total, k + 1) + EXTRA + f"""
          <div style="position:absolute;left:72px;right:72px;top:200px">
            <div class="kick">QUESTION {k}</div>
            <h1 style="font-size:78px;margin-top:16px;max-width:720px">{q}</h1></div>
          <div class="card right" style="position:absolute;left:72px;right:72px;top:720px;font-size:40px"><b>ANSWER</b>
            <div style="font-family:Poppins;font-weight:700;font-size:110px;color:#1d8a8c;line-height:1.05;margin:6px 0 14px">{a}</div>{note}</div>
          <div class="emoji" style="position:absolute;right:72px;top:250px;font-size:130px">{e}</div>""" +
          src("Sources: USDA FSIS, FoodSafety.gov cold storage chart"))
    s.append(cta(total, "DON'T TRUST YOUR MEMORY", "Your fridge <em>keeps count.</em>",
        "FridgeSmart dates every leftover and reminds you before it expires.", CONFIRM))
    render(s, "nov21")

# Sun 22 (IG): leftover turkey meals
def nov22():
    ideas = [("The next-day sandwich", "Turkey, stuffing and a smear of cranberry on soft bread."),
             ("Turkey soup", "Simmer the carcass for broth, add veg, noodles or rice."),
             ("Turkey fried rice", "Cold rice, chopped turkey, frozen peas and an egg."),
             ("Turkey quesadillas", "Tortillas, cheese and turkey. Crisp both sides."),
             ("Turkey pot pie", "Turkey, leftover veg and gravy under a crust or biscuits.")]
    total = len(ideas) + 2; s = []
    s.append(cover(total, "SAVE THIS FOR FRIDAY", "5 meals from <em>leftover turkey</em>",
        "Because nobody wants plain turkey four days in a row.", deco("🦃🥪🍲🌮")))
    for k, (name, how) in enumerate(ideas, 1):
        s.append(brand(total, k + 1) + EXTRA + f"""
          <div style="position:absolute;left:72px;right:72px;top:220px">
            <div class="num">{k:02d}</div><h1 style="font-size:96px;margin-top:10px">{name}</h1></div>
          <div class="card right" style="position:absolute;left:72px;right:72px;top:640px;font-size:42px"><b>HOW</b>{how}</div>
          <div class="emoji" style="position:absolute;left:0;right:0;top:920px;text-align:center;font-size:220px">{["🥪","🍲","🍳","🌮","🥧"][k-1]}</div>""")
    s.append(cta(total, "STILL STUCK?", "Ask Chef Lumi <em>what to make.</em>",
        "FridgeSmart suggests recipes from what's actually in your fridge."))
    render(s, "nov22")

if __name__ == "__main__":
    for name in sys.argv[1:]:
        globals()[name]()
