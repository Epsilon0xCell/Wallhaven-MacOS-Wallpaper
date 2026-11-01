#!/usr/bin/env python3
"""Wallhaven-MacOS-Wallpaper introduction banner: the advent calendar workshop, wordless.
A bench with a half built calendar at its centre, some doors closed in midwinter red and
some open on small gold and pine pictures, a glue brush across one door, a fan of cut
picture squares, red card offcuts, an idle press behind, hands smoothing a ribbon at the
side, four candles giving the main light, and snow falling past the window. No text."""
import sys, random, math
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
random.seed(97)
v = sys.argv[1] if len(sys.argv) > 1 else "ship"
W, H = 1600, 900
RED = (165, 35, 44); PINE = (35, 77, 51); GOLD = (217, 164, 65); SNOW = (247, 245, 238)
img = Image.new("RGB", (W, H), (22, 40, 29)); d = ImageDraw.Draw(img, "RGBA")
# window at the top with falling snow and dark pine shapes outside
d.rectangle([420, 0, 1180, 190], fill=(16, 26, 34))
for (px, ph) in ((470, 120), (600, 150), (760, 110), (920, 145), (1060, 118)):
    d.polygon([(px, 190), (px + 44, 60), (px + 88, 190)], fill=(14, 34, 24))
    d.polygon([(px + 22, 190), (px + 44, 30), (px + 66, 190)], fill=(18, 44, 30))
random.seed(5)
for i in range(60):
    sx, sy, sr = random.uniform(430, 1170), random.uniform(4, 184), random.uniform(2.5, 6)
    d.ellipse([sx, sy, sx + sr, sy + sr], fill=(247, 245, 238, 200))
d.rectangle([420, 0, 1180, 190], outline=(90, 58, 34), width=10)
d.line([(800, 0), (800, 190)], fill=(90, 58, 34), width=8)
# bench surface
d.rectangle([0, 560, W, H], fill=(110, 74, 42))
for gx in range(0, W, 200): d.line([(gx, 560), (gx + 50, H)], fill=(84, 54, 28, 100), width=6)
d.rectangle([0, 190, W, 560], fill=(30, 52, 38))
# idle press at the back left, blank sheet in it, printed sheets stacked beside
d.rectangle([90, 300, 330, 470], fill=(52, 54, 58), outline=(30, 30, 32), width=4)
d.ellipse([120, 330, 220, 410], outline=(140, 142, 148), width=12); d.ellipse([200, 330, 300, 410], outline=(140, 142, 148), width=12)
d.rectangle([140, 428, 290, 520], fill=SNOW, outline=(180, 176, 166), width=3)
for i in range(4): d.rectangle([1250 + i * 4, 430 - i * 7, 1470 + i * 4, 520 - i * 7], fill=(240, 237, 228), outline=(170, 166, 156), width=2)
# the half built calendar at the centre of the bench
calx, caly, cw, ch = 470, 250, 660, 470
d.rectangle([calx, caly, calx + cw, caly + ch], fill=(238, 233, 220), outline=(120, 96, 62), width=5)
pics = ["cottage", "bell", "candle", "bridge"]
pi = 0
for r in range(4):
    for c in range(5):
        x, y = calx + 18 + c * 126, caly + 18 + r * 110; w2, h2 = 112, 96
        state = (r * 5 + c) % 3
        if state == 0:  # closed door
            d.rectangle([x, y, x + w2, y + h2], fill=RED, outline=PINE, width=4)
            for t in range(6, w2, 13): d.ellipse([x + t, y + 4, x + t + 3, y + 7], fill=(240, 235, 225, 160))
        elif state == 1:  # open door showing a small wordless picture
            d.rectangle([x, y, x + w2, y + h2], fill=(250, 244, 226), outline=GOLD, width=4)
            kind = pics[pi % 4]; pi += 1; cx, cy = x + w2 // 2, y + h2 // 2
            if kind == "cottage":
                d.polygon([(cx - 30, cy), (cx, cy - 26), (cx + 30, cy)], fill=SNOW, outline=PINE, width=2)
                d.rectangle([cx - 22, cy, cx + 22, cy + 24], fill=(150, 96, 54)); d.rectangle([cx - 6, cy + 6, cx + 6, cy + 18], fill=GOLD)
            elif kind == "bell":
                d.polygon([(cx - 8, cy - 26), (cx + 8, cy - 26), (cx + 20, cy + 14), (cx - 20, cy + 14)], fill=GOLD, outline=(168, 118, 40), width=2)
                d.ellipse([cx - 6, cy + 14, cx + 6, cy + 26], fill=(168, 118, 40))
            elif kind == "candle":
                d.rectangle([cx - 8, cy - 6, cx + 8, cy + 26], fill=SNOW, outline=(190, 186, 176), width=2)
                d.ellipse([cx - 6, cy - 24, cx + 6, cy - 4], fill=GOLD)
            else:
                d.arc([cx - 32, cy - 6, cx + 32, cy + 30], 180, 360, fill=PINE, width=5)
                d.line([(cx - 34, cy + 14), (cx + 34, cy + 14)], fill=PINE, width=4)
            d.polygon([(x, y), (x + 20, y + 10), (x + 20, y + h2 - 10), (x, y + h2)], fill=(140, 30, 38))  # open flap
        else:  # empty cell waiting for its picture
            d.rectangle([x, y, x + w2, y + h2], outline=(170, 162, 146), width=3)
# glue brush across one closed door, wet at the tip
bx, by = (560, 330) if v != "v1" else (560, 300)
d.polygon([(bx, by), (bx + 190, by - 42), (bx + 200, by - 26), (bx + 10, by + 14)], fill=(150, 96, 54))
d.polygon([(bx + 190, by - 42), (bx + 236, by - 52), (bx + 240, by - 34), (bx + 200, by - 26)], fill=(196, 200, 206))
d.ellipse([bx + 232, by - 50, bx + 252, by - 30], fill=(250, 248, 240))
# fan of cut picture squares beside the calendar
for i, ang in enumerate((-24, -8, 8, 24)):
    cx, cy = 1240, 640; r = math.radians(ang)
    pts = [(cx + 74 * math.cos(r + a) - 50 * math.sin(r + a), cy + 74 * math.sin(r + a) + 50 * math.cos(r + a)) for a in (0, 1.57, 3.14, 4.71)]
    d.polygon(pts, fill=(250, 244, 226), outline=GOLD, width=3)
d.ellipse([1228, 622, 1252, 646], fill=GOLD)  # candle picture dot in the fan
# red card offcuts curling at the bench edge
for (ox, oy) in ((180, 800), (330, 836), (1420, 820)):
    d.arc([ox, oy, ox + 90, oy + 44], 200, 480, fill=RED, width=9)
# hands at the side smoothing a ribbon: sleeves and hands only
d.polygon([(0, 620), (190, 640), (180, 730), (0, 720)], fill=(96, 44, 52))
d.ellipse([150, 646, 268, 706], fill=(222, 184, 148), outline=(190, 150, 116), width=3)
for i in range(4): d.line([(238, 656 + i * 11), (286, 662 + i * 10)], fill=(222, 184, 148), width=9)
d.rectangle([240, 690, 560, 706], fill=PINE)  # the ribbon being smoothed flat
d.polygon([(560, 690), (584, 698), (560, 706)], fill=PINE)
# four candles in a holder at the right of the bench, the main light
layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
ld.ellipse([1180, 560, 1560, 900], fill=(255, 200, 90, 52))
img = Image.alpha_composite(img.convert("RGBA"), layer.filter(ImageFilter.GaussianBlur(40))).convert("RGB"); d = ImageDraw.Draw(img, "RGBA")
d.rectangle([1330, 760, 1470, 782], fill=(70, 58, 30))
wax = (2, 4) if v == "v1" else (1, 3)
for i, cx in enumerate((1346, 1386, 1426, 1462)):
    hgt = 74 - (i % 2) * 16
    d.rectangle([cx - 10, 760 - hgt, cx + 10, 760], fill=(244, 240, 228), outline=(200, 196, 184), width=2)
    if i in wax:
        d.ellipse([cx - 6, 760 - hgt - 26, cx + 6, 760 - hgt - 2], fill=GOLD)
        d.ellipse([cx - 2, 760 - hgt - 18, cx + 2, 760 - hgt - 6], fill=(255, 226, 140))
        d.polygon([(cx + 8, 760 - hgt + 12), (cx + 13, 760 - hgt + 30), (cx + 6, 760 - hgt + 30)], fill=(244, 240, 228))
rng = np.random.default_rng(2); a = np.asarray(img).astype(np.int16); n = rng.normal(0, 3, a.shape[:2])[..., None]
img = Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))
out = "intro-banner.png" if v == "ship" else f"scratch/intro-{v}.png"
img.save(out); print(out)
