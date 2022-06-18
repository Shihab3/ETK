from PIL import Image
from PIL import ImageDraw, ImageChops
import os.path as o

def add_corners(im, rad=100):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, "white")
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    alpha = ImageChops.darker(alpha, im.split()[-1])
    im.putalpha(alpha)
    return im

def createCurnerImage(save, size=(64,64),color=(0,255,10), rad=20):
    im = Image.new('RGBA',size,color)
    im = add_corners(im,rad)
    im.save(save)
