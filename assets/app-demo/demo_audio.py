import numpy as np, wave
SR = 48000
DUR = 24.97
N = int(SR * DUR)
mix = np.zeros((N, 2))
rng = np.random.default_rng(7)

BPM = 116
beat = 60 / BPM

def add(sig, t, gain=1.0, pan=0.0):
    i = int(t * SR)
    if i >= N: return
    sig = sig[: N - i] * gain
    l = np.cos((pan + 1) * np.pi / 4); r = np.sin((pan + 1) * np.pi / 4)
    mix[i:i + len(sig), 0] += sig * l * 1.414
    mix[i:i + len(sig), 1] += sig * r * 1.414

def env(n, a=0.005, d=0.2):
    t = np.arange(n) / SR
    e = np.minimum(1, t / a) * np.exp(-t / d)
    return e

def kick():
    n = int(0.45 * SR); t = np.arange(n) / SR
    f = 50 + 110 * np.exp(-t * 28)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * np.exp(-t * 7) * 0.9

def clap():
    n = int(0.25 * SR); t = np.arange(n) / SR
    x = rng.standard_normal(n)
    e = np.exp(-t * 22) + 0.6 * np.exp(-((t - 0.012) * 300) ** 2) + 0.5 * np.exp(-((t - 0.024) * 300) ** 2)
    x = np.diff(np.concatenate([[0], x]))  # brighten
    return x * e * 0.25

def hat(open_=False):
    n = int((0.18 if open_ else 0.05) * SR); t = np.arange(n) / SR
    x = np.diff(np.concatenate([[0], rng.standard_normal(n)]))
    return x * np.exp(-t * (18 if open_ else 70)) * 0.09

def note_freq(m): return 440 * 2 ** ((m - 69) / 12)

def pluck(m, length=0.5, bright=1.0):
    n = int(length * SR); t = np.arange(n) / SR
    f = note_freq(m)
    s = np.sin(2*np.pi*f*t) + 0.5*np.sin(2*np.pi*2*f*t)*np.exp(-t*8*bright) + 0.25*np.sin(2*np.pi*3*f*t)*np.exp(-t*12)
    return s * env(n, 0.003, 0.22) * 0.12

def pad(ms, length):
    n = int(length * SR); t = np.arange(n) / SR
    s = np.zeros(n)
    for m in ms:
        f = note_freq(m)
        for det in (-0.12, 0.12):
            s += np.sin(2*np.pi*f*(1+det/100)*t + rng.uniform(0, 6))
    e = np.minimum(1, t / 0.3) * np.minimum(1, (length - t) / 0.3)
    return s * e * 0.018

def bass(m, length):
    n = int(length * SR); t = np.arange(n) / SR
    f = note_freq(m)
    s = np.sin(2*np.pi*f*t) + 0.3*np.sin(2*np.pi*2*f*t)
    return s * env(n, 0.005, 0.35) * 0.32

# chords: C - G - Am - F (one bar each, 4 beats)
prog = [(48, [60, 64, 67, 72]), (43, [59, 62, 67, 71]), (45, [60, 64, 69, 72]), (41, [60, 65, 69, 72])]
bar = 4 * beat
nbars = int(DUR / bar) + 1
INTRO_END = 0.0
for b in range(nbars):
    t0 = b * bar
    root, ch = prog[b % 4]
    add(pad(ch, bar + 0.2), t0, 1.0)
    full = t0 + 0.01 >= INTRO_END - 0.2
    for k in range(8):  # eighth notes
        tt = t0 + k * beat / 2
        if tt >= DUR: break
        # arpeggio pluck
        m = ch[[0, 2, 1, 3, 2, 1, 3, 2][k]] + 12
        add(pluck(m, 0.4), tt, 0.9 if full else 0.55, pan=0.35 if k % 2 else -0.35)
        add(hat(open_=(k % 4 == 3)), tt, 1.0 if full else 0.0, pan=0.25)
    for q in range(4):
        tt = t0 + q * beat
        if tt >= DUR: break
        if full or q in (0,):
            add(kick(), tt, 1.0 if full else 0.6)
        if full and q in (1, 3):
            add(clap(), tt, 1.0)
        if full:
            add(bass(root, beat * 0.9), tt, 1.0)
            if q == 3: add(bass(root + 7, beat * 0.45), tt + beat / 2, 0.8)


def whoosh(length=0.45):
    n = int(length * SR); t = np.arange(n) / SR
    x = rng.standard_normal(n)
    # sweeping one-pole lowpass
    y = np.zeros(n); a_s = 0.02 + 0.5 * (t / length) ** 1.5
    acc = 0.0
    for i in range(n):
        acc += a_s[i] * (x[i] - acc); y[i] = acc
    e = np.sin(np.pi * np.clip(t / length, 0, 1)) ** 2
    return y * e * 0.55

def pop(f0=600, f1=1400, length=0.12, g=0.35):
    n = int(length * SR); t = np.arange(n) / SR
    f = f0 + (f1 - f0) * (t / length)
    return np.sin(2*np.pi*np.cumsum(f)/SR) * np.exp(-t * 30) * g

def thud():
    n = int(0.35 * SR); t = np.arange(n) / SR
    body = np.sin(2*np.pi*(90+60*np.exp(-t*30))*t) * np.exp(-t*12)
    clank = sum(np.sin(2*np.pi*f*t)*np.exp(-t*d) for f, d in ((820, 18), (1310, 24), (1975, 30))) * 0.25
    noise = rng.standard_normal(n) * np.exp(-t*40) * 0.2
    return (body * 0.6 + clank + noise) * 0.5

def tap():
    n = int(0.06 * SR); t = np.arange(n) / SR
    return np.sin(2*np.pi*1800*t) * np.exp(-t*90) * 0.3

def chime():
    n = int(1.2 * SR); t = np.arange(n) / SR
    s = sum(np.sin(2*np.pi*note_freq(m)*t)*np.exp(-t*3.5)*(0.6**i) for i, m in enumerate((84, 88, 91)))
    return s * 0.12


for st in (2.0, 6.0, 12.0, 17.5): add(whoosh(0.35), st-0.18, 0.6); add(pop(500,1100,0.12,0.25), st+0.05, 0.9)
add(chime(), 21.98, 1.0); add(pop(500,1300,0.14,0.3), 22.6, 1.0)
t = np.arange(N) / SR
fade = np.clip((DUR - t) / 1.2, 0, 1) * np.clip(t / 0.1, 0, 1)
mix *= fade[:, None]
mix = np.tanh(mix * 1.6) / np.tanh(1.6)
mix = mix / np.max(np.abs(mix)) * 0.89
with wave.open("demo-audio.wav", "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix*32767).astype(np.int16).tobytes())
print("ok")
