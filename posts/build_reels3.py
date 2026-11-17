"""Build novvids3.html: novvids2.html + Thanksgiving / Lifetime reels for IG noon (Nov 18-22)."""
import re
src = open("/home/claude/fs/novvids2.html").read()

def hk(i, kick, hook, sub, emo):
    return f"""<div class="scene hk" id="{i}"><div class="bg"></div><div class="dots"></div>
 <div class="kick" style="top:380px">{kick}</div>
 <div class="hook" style="top:450px;font-size:118px">{hook}</div>
 <div class="hook" style="top:1000px;font-size:56px;font-family:Inter;font-weight:700;color:#cfe6e4">{sub}</div>
 <div class="emo" style="position:absolute;left:0;right:0;top:1200px;text-align:center;font-size:220px">{emo}</div></div>\n"""

def hb(i, kick, cap, emo, stamp, cls, fixlab, fix, src_=""):
    s = f"""<div class="scene hb" id="{i}"><div class="bg"></div><div class="dots"></div>
 <div class="kick" style="top:250px">{kick}</div><div class="cap" style="top:300px;font-size:84px">{cap}</div>
 <div class="hab"></div><div class="emo hi" style="position:absolute;left:0;right:0;top:640px;text-align:center;font-size:300px">{emo}</div>
 <div class="stamp {cls}" style="top:1080px">{stamp}</div>
 <div class="fix"><b>{fixlab}</b>{fix}</div>"""
    if src_: s += f'\n <div style="position:absolute;left:0;right:0;bottom:90px;text-align:center;font-size:24px;color:#8fd9d6;font-weight:600">{src_}</div>'
    return s + "</div>\n"

def ot(i, a, b, srcline=""):
    s = f"""<div class="scene ot" id="{i}"><div class="bg"></div><div class="dots"></div>
 <div class="hook" style="top:430px;font-size:100px">{a}</div>
 <div class="hook" style="top:900px;font-size:46px;font-family:Inter;font-weight:600;color:#cfe6e4">{b}</div>
 <div class="lumi" style="width:340px;height:340px;left:370px;top:1150px"><img src="chef-lumi-avatar.png"></div>"""
    if srcline: s += f'\n <div style="position:absolute;left:0;right:0;bottom:120px;text-align:center;font-size:24px;color:#8fd9d6;font-weight:600">{srcline}</div>'
    return s + "</div>\n"

def cv(i, h, emo, stamp="", cls="no", size=118):
    s = f"""<div class="scene" id="{i}"><div class="bg"></div><div class="dots"></div>
 <div class="cvbrand"><img src="icon.png">FridgeSmart</div>
 <div class="cvh" style="font-size:{size}px">{h}</div>
 <div class="emo" style="position:absolute;left:0;right:0;top:930px;text-align:center;font-size:190px;letter-spacing:16px">{emo}</div>"""
    if stamp: s += f'\n <div class="stamp {cls}" style="top:1260px">{stamp}</div>'
    return s + "</div>\n"

USDA = "Source: USDA FSIS"
html = ""; SETS = {}

def seq(mode, parts):
    t = 0.0; out = []
    for sid, d in parts:
        out.append([sid, round(t, 2), round(t + d, 2)]); t += d
    SETS[mode] = out

# ---- 1. Turkey myths ----
myths = [("Wash the turkey <em>first</em>", "🚰", "Washing raw poultry splashes germs around your sink. Cooking kills them."),
         ("Thaw it <em>on the counter</em>", "🕒", "Thaw in the fridge: 24 hrs per 4–5 lbs. Or in cold water, 30 min per lb."),
         ("Clear juices = <em>it's done</em>", "🌡️", "Color can't tell you. It's done at 165°F in the thickest part."),
         ("Stuff it <em>the night before</em>", "🥖", "Never stuff it ahead. USDA suggests cooking stuffing in its own dish."),
         ("Leftovers can wait <em>till after pie</em>", "🥧", "Get them in the fridge within 2 hours.")]
html += hk("tm0", "THANKSGIVING MYTH BUSTERS", "5 turkey myths <em>your family still believes</em> 🦃", "How many did you believe?", "🙊")
for k, (c, e, f) in enumerate(myths, 1):
    html += hb(f"tm{k}", f"MYTH {k} / 5", c, e, "✕ MYTH", "no", "THE FACT", f)
html += ot("tm6", "After the feast: <em>don't lose the leftovers.</em>", "FridgeSmart dates every container and reminds you before it's too late.", "Food safety guidance: USDA FSIS")
html += cv("cv_turkey", "5 turkey <em>myths</em>", "🦃🚰🌡️🥧", "✕ MYTH")
seq("turkey", [("tm0", 2.6)] + [(f"tm{k}", 3.4) for k in range(1, 6)] + [("tm6", 2.8), ("end", 3.6), ("cv_turkey", 0.5)])

# ---- 2. Prep checklist ----
prep = [("Clean out <em>the fridge</em>", "🧹", "Toss anything expired or forgotten in the back."),
        ("Thaw the turkey <em>in the fridge</em>", "🦃", "24 hrs per 4–5 lbs. A 15-lb bird needs 3–4 days."),
        ("Clear <em>the bottom shelf</em>", "🧊", "Set the turkey on a tray so juices can't drip on other food."),
        ("Check it's <em>40°F or colder</em>", "🌡️", "That's the safe zone for everything in your fridge."),
        ("Grab <em>shallow containers</em>", "🥡", "Leftovers cool faster in shallow containers."),
        ("Plan <em>the leftovers</em>", "📅", "Eat them within 3–4 days or freeze them.")]
html += hk("tp0", "SAVE THIS", "Thanksgiving fridge prep <em>checklist</em> 📋", "Do it before Thursday", "🦃")
for k, (c, e, f) in enumerate(prep, 1):
    html += hb(f"tp{k}", f"STEP {k} / 6", c, e, "✓ DO IT", "ok", "HOW", f)
html += ot("tp7", "Step 1, <em>done for you.</em>", "Snap your fridge once. FridgeSmart lists every item with its date.", "Thawing, temperature and leftover times: USDA FSIS")
html += cv("cv_prep", "Thanksgiving fridge <em>prep checklist</em>", "📋🦃🧊", "✓ DO IT", "ok", 112)
seq("prep", [("tp0", 2.6)] + [(f"tp{k}", 3.0) for k in range(1, 7)] + [("tp7", 2.8), ("end", 3.6), ("cv_prep", 0.5)])

# ---- 3. Lifetime 10 days ----
html += """<div class="scene" id="d1"><div class="bg"></div><div class="dots"></div>
 <div class="kick" style="top:330px">FOUNDER'S LIFETIME</div>
 <div class="cap" style="top:400px;font-size:100px">Days left to get it:</div>
 <div id="days10" style="position:absolute;left:0;right:0;top:640px;text-align:center;font-family:Poppins;font-weight:800;font-size:520px;line-height:1;color:#ffb347;letter-spacing:-20px">10</div>
 <div class="cap" style="top:1300px;font-size:52px;font-weight:700;font-family:Inter;color:#cfe6e4">Ends Cyber Monday, Nov 30</div>
</div>\n"""
html += cv("cv_life10", "Founder's Lifetime: <em>10 days left</em>", "⏳", "$99.99 once", "ok")
seq("life10", [("d1", 3.6), ("l2", 4.8), ("lend", 4.1), ("cv_life10", 0.5)])

# ---- 4. Leftovers quiz ----
qs = [("Cooked turkey <em>in the fridge?</em>", "🦃", "3–4 DAYS", "Or “until the Monday after Thanksgiving.”"),
      ("Cooked turkey <em>in the freezer?</em>", "❄️", "2–6 MONTHS", "For best quality. Frozen at 0°F, it stays safe longer."),
      ("On the table before <em>the fridge?</em>", "⏱️", "2 HOURS", "Just 1 hour if it's over 90°F."),
      ("Turkey soup <em>in the fridge?</em>", "🍲", "3–4 DAYS", "Or 2–3 months in the freezer.")]
html += hk("tq0", "QUIZ", "How long do leftovers <em>actually last?</em> 🤔", "Guess before the answer pops up", "🥡")
for k, (q, e, a, n) in enumerate(qs, 1):
    html += hb(f"tq{k}", f"QUESTION {k} / 4", q, e, a, "ok", "ANSWER", n).replace('class="scene hb"', 'class="scene hb qz"', 1)
html += ot("tq5", "How many did you get? <em>Your fridge keeps count.</em>", "FridgeSmart dates every leftover and reminds you before it expires.", "Sources: USDA FSIS, FoodSafety.gov")
html += cv("cv_quiz", "How long do leftovers <em>last?</em>", "🦃🥡🤔")
seq("tquiz", [("tq0", 2.6)] + [(f"tq{k}", 3.8) for k in range(1, 5)] + [("tq5", 2.8), ("end", 3.6), ("cv_quiz", 0.5)])

# ---- 5. Leftover turkey meals ----
meals = [("The next-day <em>sandwich</em>", "🥪", "Turkey, stuffing and a smear of cranberry on soft bread."),
         ("Turkey <em>soup</em>", "🍲", "Simmer the carcass for broth. Add veg, noodles or rice."),
         ("Turkey <em>fried rice</em>", "🍳", "Cold rice, chopped turkey, frozen peas and an egg."),
         ("Turkey <em>quesadillas</em>", "🌮", "Tortillas, cheese and turkey. Crisp both sides."),
         ("Turkey <em>pot pie</em>", "🥧", "Turkey, leftover veg and gravy under a crust or biscuits.")]
html += hk("tl0", "SAVE THIS FOR FRIDAY", "5 meals from <em>leftover turkey</em> 🦃", "Nobody wants plain turkey 4 days in a row", "😩")
for k, (c, e, f) in enumerate(meals, 1):
    html += hb(f"tl{k}", f"MEAL {k} / 5", c, e, "😋 MAKE IT", "ok", "HOW", f)
html += ot("tl6", "Still stuck? <em>Ask Chef Lumi.</em>", "FridgeSmart suggests recipes from what's actually in your fridge.")
html += cv("cv_meals", "5 meals from <em>leftover turkey</em>", "🥪🍲🌮🥧", size=112)
seq("tmeals", [("tl0", 2.6)] + [(f"tl{k}", 3.0) for k in range(1, 6)] + [("tl6", 2.8), ("end", 3.6), ("cv_meals", 0.5)])

out = src.replace("<script>const MODE", html + "<script>const MODE", 1)
sets_js = "".join(f" {m}:{v},\n" for m, v in SETS.items()).replace("'", '"')
out = out.replace("const SETS={\n", "const SETS={\n" + sets_js, 1)
handlers = """  if(el.classList.contains('hk')){ $$('.hook,.kick',el).forEach(x=>hook(x,lt)); popin($('.emo',el),lt,0.3,0.45); }
  if(el.classList.contains('ot')){ $$('.hook',el).forEach((x,i)=>enter(x,lt,i*0.4,0.4,i?30:50)); popin($('.lumi',el),lt,0.8,0.5); }
  if(id==='d1'){ $('.kick',el).style.opacity=1; hook($('.cap',el),lt);
    const n=Math.round(30-20*eo((lt-0.3)/1.6)); const dd=$('#days10'); dd.textContent=n; const p=back((lt-1.9)/0.4); dd.style.transform=`scale(${lt>1.9?0.85+0.15*p:1})`; enter($$('.cap',el)[1],lt,2.0,0.4,30); }
  if(id==='end'){"""
out = out.replace("  if(id==='end'){", handlers, 1)
old_hb = "const st=$('.stamp',el); const p=back((lt-0.9)/0.35); st.style.opacity=cl((lt-0.9)/0.1);"
assert old_hb in out
out = out.replace(old_hb, "const qd=el.classList.contains('qz')?1.1:0; const st=$('.stamp',el); const p=back((lt-0.9-qd)/0.35); st.style.opacity=cl((lt-0.9-qd)/0.1);")
out = out.replace("enter($('.fix',el),lt,1.2,0.35,30); }", "enter($('.fix',el),lt,1.2+(el.classList.contains('qz')?1.1:0),0.35,30); }", 1)
open("/home/claude/fs/novvids3.html", "w").write(out)
print({m: v[-1][2] for m, v in SETS.items()})
