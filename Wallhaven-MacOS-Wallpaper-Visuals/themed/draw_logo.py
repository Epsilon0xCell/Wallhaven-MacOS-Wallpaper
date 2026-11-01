#!/usr/bin/env python3
"""Wallhaven-MacOS-Wallpaper logo: one closed advent calendar door in midwinter red with a
pine border, a gold oval holding a snow roofed cottage with one lit window, perforations on
three sides, a thumb notch on the fourth, a candle gold shadow, and the name in Arimo in
pine green beneath with wide spacing."""
import sys
from PIL import Image, ImageDraw, ImageFont
v = sys.argv[1] if len(sys.argv) > 1 else "ship"
S = 1000
RED = (165, 35, 44); PINE = (35, 77, 51); GOLD = (217, 164, 65); SNOW = (247, 245, 238)
img = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
d.rounded_rectangle([266, 130, 754, 644], 30, fill=(217, 164, 65, 110))  # candle gold shadow
x0, y0, x1, y1 = 240, 100, 720, 610
tilt = 0 if v == "v1" else 0
d.rounded_rectangle([x0, y0, x1, y1], 26, fill=RED, outline=PINE, width=16)
# perforations on three sides (top, left, right), notch on the bottom edge
for t in range(x0 + 30, x1 - 20, 26): d.ellipse([t, y0 + 12, t + 7, y0 + 19], fill=SNOW)
for t in range(y0 + 30, y1 - 20, 26):
    d.ellipse([x0 + 12, t, x0 + 19, t + 7], fill=SNOW); d.ellipse([x1 - 19, t, x1 - 12, t + 7], fill=SNOW)
d.pieslice([430, y1 - 26, 530, y1 + 26], 180, 360, fill=(0, 0, 0, 0), outline=SNOW, width=6)
d.arc([430, y1 - 24, 530, y1 + 24], 180, 360, fill=SNOW, width=7)
# gold oval with the winter scene
d.ellipse([330, 180, 630, 480], fill=(250, 240, 214), outline=GOLD, width=12)
d.ellipse([346, 196, 614, 464], outline=PINE, width=4)
cx, cy = 480, 330
d.polygon([(cx - 92, cy + 6), (cx, cy - 74), (cx + 92, cy + 6)], fill=SNOW, outline=PINE, width=5)  # snow roof
d.rectangle([cx - 64, cy + 6, cx + 64, cy + 96], fill=(120, 74, 44))
d.rectangle([cx - 16, cy + 30, cx + 16, cy + 66], fill=GOLD, outline=(150, 100, 30), width=3)  # one lit window
d.rectangle([cx + 34, cy + 44, cx + 52, cy + 96], fill=(90, 56, 32))
for (sx, sy) in ((392, 236), (560, 220), (520, 420)):
    d.ellipse([sx, sy, sx + 9, sy + 9], fill=SNOW)
f = ImageFont.truetype("fonts/Arimo.ttf", 54)
try: d.text((480, 736), "Wallhaven-MacOS-Wallpaper", font=f, anchor="mm", fill=PINE, spacing=4)
except Exception: d.text((480, 736), "Wallhaven-MacOS-Wallpaper", font=f, anchor="mm", fill=PINE)
out = "logo.png" if v == "ship" else f"scratch/logo-{v}.png"
img.save(out)
img.resize((64, 64)).save("scratch/logo64-ship.png" if v == "ship" else f"scratch/logo64-{v}.png")
print(out)
