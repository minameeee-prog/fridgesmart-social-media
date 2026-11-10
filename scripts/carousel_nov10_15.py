"""Nov 10–15 carousels (1080x1350) on the shared carousel base."""
import sys
from carousel import brand, render
from carousel_nov5_8 import EXTRA, cta, cover

SCAN = "/home/claude/fridgesmart-social-media/assets/app-demo/still-scanning.png"
CONFIRM = "/home/claude/fridgesmart-social-media/assets/app-demo/still-confirm-items.png"

FRIDGE_CSS = """<style>
.fr{position:absolute;width:400px;height:760px;border-radius:40px;background:#e9f1ef;box-shadow:0 30px 70px rgba(0,0,0,.45);padding:22px;display:flex;gap:14px}
.fr .cab{flex:1;display:flex;flex-direction:column;gap:12px}
.fr .door{width:96px;display:flex;flex-direction:column;gap:12px;border-left:4px dashed #b9cbc8;padding-left:12px}
.fr .z{border-radius:18px;background:#cfdedb;flex:1;display:grid;place-items:center;font-family:'Noto Color Emoji';font-size:54px;opacity:1}
.fr .z span{opacity:.35}.fr .z.on span{opacity:1;font-size:74px}
.fr .z.on{background:#ffb347;box-shadow:0 0 0 6px rgba(255,179,71,.35)}
.fr .dr{flex:1.2;display:flex;gap:10px}.fr .dr .z{flex:1}
.zl{position:absolute;font-weight:800;font-size:24px;letter-spacing:3px;color:#8fd9d6}
</style>"""

def fridge(on, left=620, top=330):
    z = lambda k, e: f"<div class='z{' on' if k in on else ''}'><span>{e}</span></div>"
    return (FRIDGE_CSS + f"<div class='fr' style='left:{left}px;top:{top}px'><div class='cab'>{z('top','🥛🧀')}{z('mid','🍲')}{z('low','🥩')}"
            f"<div class='dr'>{z('crisp','🥕')}{z('crisp','🍎')}</div></div><div class='door'>{z('door','🫙')}{z('door','🧈')}{z('door','🥫')}</div></div>")

def src(t): return f"<div class='src'>{t}</div>"

def nov10():
    zones = [("top", "Top shelf", "Ready&#8209;to&#8209;eat food", "Milk, juice, cheese and anything you eat without heating it."),
             ("mid", "Middle shelf", "Leftovers", "Cooked food you'll reheat. Eat leftovers within 3–4 days."),
             ("low", "Bottom shelf", "Raw meat, poultry & fish", "Sealed or wrapped tight, so juices can't drip onto other food."),
             ("crisp", "Crisper drawers", "Fruits & vegetables", "Keep them away from raw meat."),
             ("door", "The door", "Condiments only", "It's the warmest spot and the temperature swings. Eggs go in their carton on a shelf.")]
    total = len(zones) + 3; s = []
    s.append(brand(total, 1) + EXTRA + """
      <div style="position:absolute;left:72px;top:230px;width:520px">
        <div class="kick">TIP TUESDAY</div>
        <h1 style="font-size:112px;margin-top:20px">Your fridge has <em>zones.</em></h1>
        <div style="margin-top:36px;font-size:36px;color:#cfe6e4;line-height:1.35">Most of us use them wrong. Here's what goes where.</div>
      </div>""" + fridge({"top", "mid", "low", "crisp", "door"}) + "<div class='swipe'>Swipe →</div>")
    for k, (key, zone, what, note) in enumerate(zones, 1):
        s.append(brand(total, k + 1) + EXTRA + f"""
          <div style="position:absolute;left:72px;top:210px;width:500px">
            <div class="num">{k:02d}</div>
            <div class="kick" style="margin-top:6px">{zone.upper()}</div>
            <h1 style="font-size:{72 if len(what)>16 else 84}px;margin-top:12px">{what}</h1>
          </div>{fridge({key})}
          <div class="card right" style="position:absolute;left:72px;right:72px;top:1120px;font-size:34px;padding:28px 34px">{note}</div>""")
    s.append(brand(total, total - 1) + EXTRA + """
      <div style="position:absolute;left:72px;right:72px;top:240px"><div class="kick">THE NUMBER TO KNOW</div>
        <h1 style="font-size:120px;margin-top:16px">Keep it at <em>40°F</em> or below.</h1>
        <div style="margin-top:36px;font-size:36px;color:#cfe6e4;line-height:1.35;max-width:820px">An appliance thermometer is the easy way to check.</div></div>
      <div class="emoji" style="position:absolute;left:0;right:0;top:860px;text-align:center;font-size:240px">🌡️</div>""" +
      src("Sources: USDA FSIS · University of Illinois Extension"))
    s.append(cta(total, "KNOW WHAT'S IN EVERY ZONE", "Your fridge, <em>tracked.</em>",
        "FridgeSmart scans your fridge and reminds you before food expires.", SCAN))
    render(s, "nov10")

def nov11():
    meals = [("Chicken tacos", "Shred it, warm it with salsa, pile into tortillas.", "15 min", "🌮"),
             ("Chicken fried rice", "Day-old rice, eggs, frozen peas, soy sauce, chicken.", "15 min", "🍚"),
             ("Chicken noodle soup", "Simmer the bones for broth, then noodles and carrots.", "40 min", "🍜"),
             ("Quesadillas", "Chicken, cheese, tortilla. Crisp both sides.", "10 min", "🧀"),
             ("Creamy chicken pasta", "Pasta, garlic, a splash of cream, chicken and spinach.", "20 min", "🍝")]
    total = len(meals) + 3; s = []
    s.append(cover(total, "CHEF LUMI WEDNESDAY", "1 rotisserie chicken. <em>5 dinners.</em>",
        "Pick it apart on day one, then cook all week.",
        "<div class='emoji' style='position:absolute;left:72px;bottom:150px;font-size:130px'>🍗</div>"
        "<div class='lumi' style='width:320px;height:320px;right:60px;bottom:110px'><img src='chef-lumi-avatar.png'></div>"))
    for k, (name, how, t, e) in enumerate(meals, 1):
        s.append(brand(total, k + 1) + EXTRA + f"""
          <div style="position:absolute;left:72px;right:72px;top:220px">
            <div class="num">{k:02d}</div>
            <h1 style="font-size:100px;margin-top:10px">{name}</h1>
            <div style="margin-top:34px"><span class="pill">⏱ {t}</span><span class="pill">🍗 leftover chicken</span></div>
          </div>
          <div class="emoji" style="position:absolute;right:80px;top:640px;font-size:200px">{e}</div>
          <div class="card right" style="position:absolute;left:72px;right:72px;top:900px;font-size:40px"><b>HOW</b>{how}</div>""")
    s.append(brand(total, total - 1) + EXTRA + """
      <div style="position:absolute;left:72px;right:72px;top:240px"><div class="kick">ONE RULE</div>
        <h1 style="font-size:104px;margin-top:16px">Eat cooked chicken within <em style="white-space:nowrap">3–4 days.</em></h1>
        <div style="margin-top:36px;font-size:36px;color:#cfe6e4;line-height:1.35;max-width:820px">Or freeze it in portions on day one and thaw it in the fridge.</div></div>
      <div class="emoji" style="position:absolute;left:0;right:0;top:880px;text-align:center;font-size:220px">🗓️</div>""" +
      src("Source: FoodSafety.gov cold storage chart"))
    s.append(cta(total, "NOT SURE WHAT TO MAKE?", "Chef Lumi cooks with <em>what you have.</em>",
        "FridgeSmart matches recipes to the food already in your fridge."))
    render(s, "nov11")

def nov12():
    groups = [("1–2 days", "Use these first", [("🥩", "Ground beef"), ("🍗", "Raw chicken pieces")]),
              ("3–5 days", "This week", [("🥩", "Steaks"), ("🍲", "Leftovers & soup (3–4 days)"), ("🥪", "Opened lunch meat")]),
              ("1 week", "Next week, tops", [("🌭", "Opened hot dogs"), ("🥓", "Bacon")]),
              ("3–5 weeks", "The long haul", [("🥚", "Raw eggs in the shell")])]
    total = len(groups) + 2; s = []
    s.append(cover(total, "SAVE THIS", "How long food <em>really</em> lasts in your fridge",
        "At 40°F or below. Screenshot it for your next grocery run.",
        "<div class='emoji' style='position:absolute;left:72px;bottom:150px;font-size:110px;letter-spacing:14px;white-space:nowrap'>🥩🍗🥚🥓</div>"))
    for k, (span, label, items) in enumerate(groups, 1):
        rows = "".join(f"<div class='item' style='font-size:46px;padding:30px 34px;margin-bottom:22px'><div><span class='emoji'>{e}</span>&nbsp; {n}</div></div>" for e, n in items)
        s.append(brand(total, k + 1) + EXTRA + f"""
          <div style="position:absolute;left:72px;right:72px;top:200px">
            <div class="kick">{label.upper()}</div>
            <div class="num" style="font-size:170px;margin-top:10px">{span}</div></div>
          <div style="position:absolute;left:72px;right:72px;top:560px">{rows}</div>
          <div class="emoji" style="position:absolute;right:80px;bottom:130px;font-size:130px;opacity:.9">{items[0][0]}</div>""" +
          src("Source: FoodSafety.gov cold storage chart (refrigerator, 40°F)"))
    s.append(cta(total, "STOP MEMORIZING CHARTS", "Let your fridge <em>count the days.</em>",
        "FridgeSmart adds a date to every item and alerts you before it expires.", CONFIRM))
    render(s, "nov12")

def nov13():
    rules = [("🏷️", "Label it", "Name and date on every leftover container. No more mystery tubs."),
             ("⏳", "3–4 day rule", "Leftovers get eaten or tossed within <span style='white-space:nowrap'>3–4 days.</span>"),
             ("⬅️", "Oldest in front", "New groceries go behind what's already there."),
             ("📋", "Check before you shop", "One shared list, so nobody buys a second jar of mayo."),
             ("✅", "Finished it? Say so", "Took the last yogurt? Take it off the list too.")]
    total = len(rules) + 2; s = []
    s.append(cover(total, "FAMILY FRIDAY", "Shared fridge rules <em>that end the fights</em>",
        "For families, roommates and anyone whose yogurt keeps disappearing.",
        "<div class='emoji' style='position:absolute;left:72px;bottom:150px;font-size:120px;letter-spacing:14px;white-space:nowrap'>🥛🧁🍕👀</div>"))
    for k, (e, name, body) in enumerate(rules, 1):
        s.append(brand(total, k + 1) + EXTRA + f"""
          <div style="position:absolute;left:72px;right:72px;top:200px;display:flex;align-items:flex-end;justify-content:space-between">
            <div><div class="num">{k:02d}</div><h1 style="font-size:96px;margin-top:6px;max-width:700px">{name}</h1></div>
            <div class="emoji" style="font-size:200px">{e}</div></div>
          <div class="card right" style="position:absolute;left:72px;right:72px;top:760px;font-size:42px">{body}</div>""" +
          (src("Leftover timing: FoodSafety.gov") if k == 2 else ""))
    s.append(cta(total, "RULE 4, DONE FOR YOU", "One fridge list <em>for the whole house.</em>",
        "Family Fridge in FridgeSmart: everyone sees what's in the fridge."))
    render(s, "nov13")

def nov14():
    myths = [("Freezing kills bacteria.", "It only puts them to sleep. Once food thaws, they can grow again."),
             ("Frozen food eventually goes bad.", "Kept at 0°F, it stays safe. Only the quality drops over time."),
             ("Never refreeze thawed food.", "If you thawed it in the fridge, you can refreeze it. It may lose some quality."),
             ("Thawing on the counter is fine.", "Thaw in the fridge, in cold water or in the microwave. Never on the counter."),
             ("Freezer burn means toss it.", "It's safe, just dry. Cut those spots off.")]
    total = len(myths) + 2; s = []
    s.append(cover(total, "MYTH BUSTERS", "5 freezer myths <em>you probably believe</em>",
        "Straight from the USDA. Swipe and see how many you got right.",
        "<div class='emoji' style='position:absolute;left:72px;bottom:150px;font-size:120px;letter-spacing:14px;white-space:nowrap'>🧊❄️🥶</div>"))
    for k, (m, f) in enumerate(myths, 1):
        s.append(brand(total, k + 1) + EXTRA + f"""
          <div style="position:absolute;left:72px;right:72px;top:200px"><div class="num">{k:02d}</div></div>
          <div class="card wrong" style="position:absolute;left:72px;right:72px;top:420px;font-size:52px;font-family:Poppins;font-weight:700"><b>✕ MYTH</b>“{m}”</div>
          <div class="card right" style="position:absolute;left:72px;right:72px;top:780px;font-size:42px"><b>✓ FACT</b>{f}</div>
          <div class="emoji" style="position:absolute;right:80px;top:180px;font-size:150px">{"🦠🧊🔁🕒🥩"[k-1]}</div>""" +
          src("Source: USDA FSIS, Freezing and Food Safety"))
    s.append(cta(total, "FROM FREEZER TO FRIDGE", "Track it all <em>in one place.</em>",
        "FridgeSmart keeps every item's date and reminds you before it expires.", SCAN))
    render(s, "nov14")

def nov15():
    ideas = [("Fried rice", "Leftover rice, eggs and any vegetables that need using."),
             ("Frittata", "Eggs plus whatever cheese, greens and veg are hanging around."),
             ("Clean-out soup", "Tired vegetables, broth and a can of beans."),
             ("Quesadillas", "Tortillas, cheese, leftover meat or beans. Crisp both sides."),
             ("Smoothies", "Soft fruit and the last of the yogurt.")]
    total = len(ideas) + 2; s = []
    s.append(cover(total, "USE-IT-UP SUNDAY", "5 meals from <em>whatever's left</em>",
        "Clear the fridge before the new groceries go in.",
        "<div class='emoji' style='position:absolute;left:72px;bottom:150px;font-size:120px;letter-spacing:14px;white-space:nowrap'>🍳🥘🌮🥤</div>"))
    for k, (name, how) in enumerate(ideas, 1):
        s.append(brand(total, k + 1) + EXTRA + f"""
          <div style="position:absolute;left:72px;right:72px;top:220px">
            <div class="num">{k:02d}</div><h1 style="font-size:104px;margin-top:10px">{name}</h1></div>
          <div class="card right" style="position:absolute;left:72px;right:72px;top:620px;font-size:42px"><b>USES UP</b>{how}</div>
          <div class="emoji" style="position:absolute;left:0;right:0;top:900px;text-align:center;font-size:230px">{"🍳🥚🍲🧀🥤"[k-1]}</div>""")
    s.append(cta(total, "NOT SURE WHAT YOU HAVE?", "Chef Lumi <em>knows.</em>",
        "Scan your fridge and FridgeSmart suggests recipes from what's in it."))
    render(s, "nov15")

if __name__ == "__main__":
    for name in sys.argv[1:]:
        globals()[name]()
