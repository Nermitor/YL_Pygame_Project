import glob

from PIL import Image

t1, t2, t3, t4 = 50, 37, 0, 0

paths = glob.glob("*.png")

for sprite in paths:
    im = Image.open(sprite)
    a1, a2, a3, a4 = im.getbbox()
    t1 = min(t1, a1)
    t2 = min(t2, a2)
    t3 = max(t3, a3)
    t4 = max(t4, a4)

box = (t1, t2, t3, t4)

for sprite in paths:
    im = Image.open(sprite)
    im2 = im.crop(box)
    im2.save(sprite)
