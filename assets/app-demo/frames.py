"""Backgrounds (per caption), rounded-corner mask and end card for the live demo video."""
from playwright.sync_api import sync_playwright

CSS = """*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:transparent}
body{font-family:Inter,'Noto Color Emoji',sans-serif;color:#fff;position:relative}
.bg{position:absolute;inset:0;background:radial-gradient(1000px 900px at 50% 60%,#1d8a8c 0%,rgba(29,138,140,0) 70%),linear-gradient(180deg,#0b3234 0%,#0f4446 55%,#0a2f31 100%)}
.dots{position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.06) 1.5px,transparent 1.6px);background-size:30px 30px}
.kick{position:absolute;left:0;right:0;top:150px;text-align:center;font-weight:800;font-size:30px;letter-spacing:4px;color:#8fd9d6}
.kick b{display:inline-block;width:16px;height:16px;border-radius:50%;background:#ff5a4f;margin-right:12px;vertical-align:2px;box-shadow:0 0 14px #ff5a4f}
h1{position:absolute;left:60px;right:60px;top:205px;text-align:center;font-family:Poppins;font-weight:800;font-size:84px;line-height:1.02;letter-spacing:-1.5px}
h1 em{font-style:normal;color:#ffb347}
.bezel{position:absolute;left:213px;top:478px;width:654px;height:1384px;border-radius:84px;background:#0a0a0a;box-shadow:0 50px 100px rgba(0,0,0,.55),0 0 0 2px #2b2b2b inset}
.step{position:absolute;right:46px;top:500px;background:#ffb347;color:#1d2b2c;font-family:Poppins;font-weight:800;font-size:30px;border-radius:40px;padding:12px 24px;transform:rotate(4deg);box-shadow:0 12px 30px rgba(0,0,0,.35);z-index:3}
.emo{font-family:'Noto Color Emoji'}
.lumi{position:absolute;border-radius:50%;overflow:hidden;border:10px solid #fbf3e4;box-shadow:0 24px 50px rgba(0,0,0,.45)}
.lumi img{width:150%;margin-left:-25%;margin-top:-4%}
.cta{position:absolute;left:50%;transform:translateX(-50%);background:#ffb347;color:#1d2b2c;font-family:Poppins;font-weight:700;font-size:56px;padding:32px 76px;border-radius:80px;white-space:nowrap}
"""
CAPS = [
    ("Tap <em>AI Full Fridge Scan</em>", "1"),
    ("Snap your <em>whole fridge</em> <span class='emo'>📸</span>", "2"),
    ("AI finds every item <em>+ expiry dates</em>", "3"),
    ("Single item? <em>Quick Scan</em> it", "4"),
    ("Added to your fridge <span class='emo'>✅</span>", "5"),
]

def page(body):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>"

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
    def shot(html, out, transparent=False):
        open("/home/claude/demo/_f.html", "w").write(page(html)); pg.goto("file:///home/claude/demo/_f.html"); pg.wait_for_timeout(400)
        pg.screenshot(path=out, omit_background=transparent)
    for i, (cap, n) in enumerate(CAPS):
        shot(f"<div class='bg'></div><div class='dots'></div><div class='kick'><b></b>LIVE APP DEMO</div><h1>{cap}</h1><div class='bezel'></div><div class='step'>Step {n}/5</div>", f"/home/claude/demo/bg{i}.png")
    # rounded mask for the 618x1340 screen
    shot("<div style='position:absolute;left:0;top:0;width:618px;height:1340px;border-radius:66px;background:#fff'></div>", "/home/claude/demo/mask_full.png", True)
    end = """<div class='bg'></div><div class='dots'></div>
     <img src='file:///home/claude/fs/icon.png' style='position:absolute;width:340px;height:340px;left:370px;top:430px;border-radius:80px;background:#fbf3e4;box-shadow:0 30px 70px rgba(0,0,0,.45)'>
     <div style='position:absolute;left:0;right:0;top:830px;text-align:center;font-family:Poppins;font-weight:800;font-size:110px'>FridgeSmart</div>
     <div class='kick' style='top:980px;font-size:34px'>SCAN. TRACK. COOK.</div>
     <div class='cta' style='top:1110px'>Download free</div>
     <div style='position:absolute;top:1290px;left:0;right:0;text-align:center;font-size:36px;color:#d6ecea;font-weight:600'>App Store · Google Play</div>
     <div class='lumi' style='width:230px;height:230px;left:780px;top:1560px'><img src='file:///home/claude/fs/chef-lumi-avatar.png'></div>"""
    shot(end, "/home/claude/demo/end.png")
    b.close()
