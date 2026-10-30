# FridgeSmart live app demo footage

**Rule (from Mina, Oct 30 2026):** any video that talks about scanning the fridge must use this real app footage instead of static screenshots.

All clips are 590×1280, 30 fps, no audio. The old home screen and logo are already cut out, so never use the original recording (`ScreenRecording_02-20-2026_20-13-14_1.mov`) uncut.

| File | Length | What it shows | Speed |
|---|---|---|---|
| `scan-menu.mp4` | 2.0s | "Your Items" menu: AI Full Fridge Scan / Quick Scan / Scan Receipt / Manual Entry | 1x |
| `full-fridge-scan.mp4` | 10.0s | Camera on a real fridge → "Scanning your fridge…" (0–4s), then Confirm Items, 7 items detected with expiry dates (4–10s) | 3x, then 2x |
| `quick-scan.mp4` | 10.0s | Saving → Quick Scan of a cheese pack → Analyzing… | 2x |
| `full-demo-raw.mp4` | 22.0s | All of the above in order, ending on Confirm Items, 2 items, Success | mixed |
| `live-demo-branded.mp4` | 25.0s | Finished post: phone frame, step captions, music, end card, cover as last 0.5s | — |
| `still-scanning.png`, `still-confirm-items.png` | — | Stills for covers and carousels | — |

## How to use it in a new video
- Put a clip inside the phone frame: scale it to 618×1340, round the corners with `mask.png`, and overlay it at x=231, y=500 on a 1080×1920 background. `frames.py` has the background, bezel and caption template.
- Short spots (a 3–5s "scan" beat in a longer video) use `full-fridge-scan.mp4` from 0–4s for the scan and 4–10s for the result.
- `demo_audio.py` generates matching music; change `DUR` and the SFX times to fit.
- Every video gets a designed cover appended as its last 0.5s. Set Buffer `thumbnailOffset` to (duration − 0.25s) for Instagram and TikTok.
