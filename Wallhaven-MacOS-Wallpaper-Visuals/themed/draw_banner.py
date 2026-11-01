#!/usr/bin/env python3
"""Wallhaven-MacOS-Wallpaper wordmark banner: the workshop bench in early December.
Calendar blanks stacked at the left, a grandmother in an apron pressing a finished
calendar flat at the centre while a small press feeds printed picture sheets beside her,
tools crowding the bench, four advent candles on the windowsill with two lit and snow
outside the dark glass, and a completed calendar on the wall whose largest open doorway
reveals a picture card carrying the project name in Arimo capitals in gold on pine."""
import sys, random
from PIL import Image, ImageDraw, ImageFont
import numpy as np
random.seed(13)
v = sys.argv[1] if len(sys.argv) > 1 else "ship"
W, H = 1600, 560
RED = (165, 35, 44); PINE = (35, 77, 51); GOLD = (217, 164, 65); SNOW = (247, 245, 238)
img = Image.new("RGB", (W, H), (24, 44, 32)); d = ImageDraw.Draw(img, "RGBA")
# window with snow at the back right
d.rectangle([1120, 20, 1560, 220], fill=(16, 26, 34))
for (px, ph) in ((1150, 130), (1280, 155), (1420, 125)):
    d.polygon([(px, 220), (px + 36, 90), (px + 72, 220)], fill=(14, 34, 24))
for i in range(34):
    sx, sy = random.uniform(1130, 1550), random.uniform(28, 212); d.ellipse([sx, sy, sx + 4, sy + 4], fill=(247, 245, 238, 190))
d.rectangle([1120, 20, 1560, 220], outline=(90, 58, 34), width=8)
# four advent candles on the windowsill, two lit
d.rectangle([1120, 220, 1560, 238], fill=(90, 58, 34))
for i, cx in enumerate((1180, 1270, 1360, 1450)):
    hgt = 58 - (i % 2) * 12
    d.rectangle([cx - 9, 220 - hgt, cx + 9, 220], fill=(244, 240, 228), outline=(200, 196, 184), width=2)
    if i in (0, 2):
        d.ellipse([cx - 5, 220 - hgt - 22, cx + 5, 220 - hgt - 2], fill=GOLD)
        d.ellipse([cx - 2, 220 - hgt - 15, cx + 2, 220 - hgt - 5], fill=(255, 226, 140))
# bench
d.rectangle([0, 400, W, H], fill=(110, 74, 42))
for gx in range(0, W, 200): d.line([(gx, 400), (gx + 40, H)], fill=(84, 54, 28, 100), width=5)
# calendar blank stacks at the left
for s, (bx, by) in enumerate(((60, 300), (86, 322))):
    d.rectangle([bx, by, bx + 250, by + 128], fill=(238, 233, 220), outline=(120, 96, 62), width=3)
    for r in range(3):
        for c in range(4):
            d.rectangle([bx + 12 + c * 58, by + 12 + r * 36, bx + 58 + c * 58, by + 40 + r * 36], fill=RED, outline=PINE, width=2)
# the completed calendar on the wall, several doors open, largest doorway carries the name
wx, wy = 420, 36
d.rectangle([wx, wy, wx + 620, wy + 250], fill=(238, 233, 220), outline=(120, 96, 62), width=4)
for r in range(3):
    for c in range(5):
        x, y = wx + 14 + c * 120, wy + 14 + r * 76
        if (r, c) == (1, 2): continue
        if (r * 5 + c) % 3 == 1:
            d.rectangle([x, y, x + 106, y + 64], fill=(250, 244, 226), outline=GOLD, width=3)
            d.ellipse([x + 40, y + 16, x + 66, y + 42], fill=GOLD)
        else:
            d.rectangle([x, y, x + 106, y + 64], fill=RED, outline=PINE, width=3)
# largest open doorway with the name card
nx, ny = wx + 14 + 2 * 120, wy + 14 + 76
d.rectangle([nx - 84, ny - 8, nx + 190, ny + 80], fill=PINE, outline=GOLD, width=4)
size = 30 if v == "v1" else 27
f = ImageFont.truetype("fonts/Arimo.ttf", size)
lines = ["Wallhaven-", "MacOS-Wallpaper"] if v == "v1" else ["Wallhaven-MacOS-", "Wallpaper"]
d.text((nx + 53, ny + 18), lines[0], font=f, anchor="mm", fill=GOLD)
d.text((nx + 53, ny + 54), lines[1], font=f, anchor="mm", fill=GOLD)
# grandmother at the centre pressing a calendar flat: apron figure, palms down
gx = 760
d.ellipse([gx - 34, 258, gx + 34, 326], fill=(222, 184, 148))  # head
d.arc([gx - 36, 250, gx + 36, 322], 180, 360, fill=(206, 202, 196), width=14)  # grey bun hair
d.polygon([(gx - 58, 326), (gx + 58, 326), (gx + 78, 452), (gx - 78, 452)], fill=(96, 44, 52))  # dress
d.polygon([(gx - 34, 340), (gx + 34, 340), (gx + 44, 452), (gx - 44, 452)], fill=SNOW)  # apron
d.polygon([(gx - 58, 340), (gx - 150, 428), (gx - 132, 446), (gx - 40, 372)], fill=(96, 44, 52))
d.polygon([(gx + 58, 340), (gx + 150, 428), (gx + 132, 446), (gx + 40, 372)], fill=(96, 44, 52))
d.ellipse([gx - 168, 428, gx - 118, 452], fill=(222, 184, 148)); d.ellipse([gx + 118, 428, gx + 168, 452], fill=(222, 184, 148))
d.rectangle([gx - 190, 448, gx + 190, 540], fill=(238, 233, 220), outline=(120, 96, 62), width=3)
for r in range(2):
    for c in range(4):
        d.rectangle([gx - 172 + c * 88, 460 + r * 38, gx - 96 + c * 88, 490 + r * 38], fill=RED, outline=PINE, width=2)
# small press feeding printed sheets at the right of the bench
d.rectangle([1120, 330, 1330, 452], fill=(52, 54, 58), outline=(30, 30, 32), width=4)
d.ellipse([1146, 352, 1226, 412], outline=(140, 142, 148), width=10); d.ellipse([1230, 352, 1310, 412], outline=(140, 142, 148), width=10)
d.polygon([(1330, 380), (1520, 420), (1500, 470), (1330, 440)], fill=(250, 244, 226), outline=(170, 166, 156), width=2)
for (px, py) in ((1380, 414), (1440, 428)):
    d.rectangle([px, py, px + 34, py + 26], fill=(250, 244, 226), outline=GOLD, width=2); d.ellipse([px + 10, py + 5, px + 24, py + 19], fill=GOLD)
# tools crowding the bench: scissors, glue pot with brush, ribbon spool, ruler
d.line([(360, 500), (420, 540)], fill=(170, 172, 178), width=6); d.line([(360, 540), (420, 500)], fill=(170, 172, 178), width=6)
d.ellipse([348, 492, 368, 512], outline=(170, 172, 178), width=4); d.ellipse([348, 528, 368, 548], outline=(170, 172, 178), width=4)
d.rectangle([980, 486, 1036, 536], fill=(120, 74, 44), outline=(80, 50, 26), width=3)
d.polygon([(992, 486), (1052, 462), (1058, 472), (1000, 496)], fill=(150, 96, 54))
d.ellipse([1060, 496, 1116, 540], fill=PINE); d.ellipse([1076, 508, 1100, 528], fill=(24, 44, 32))
d.rectangle([60, 520, 330, 538], fill=(217, 190, 120), outline=(150, 120, 60), width=2)
rng = np.random.default_rng(9); a = np.asarray(img).astype(np.int16); n = rng.normal(0, 3, a.shape[:2])[..., None]
img = Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))
out = "banner.png" if v == "ship" else f"scratch/banner-{v}.png"
img.save(out); print(out)
