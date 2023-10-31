# drawing
from PIL import Image, ImageDraw, ImageFont
import os

im = Image.new('RGBA', (600, 600), 'white')
draw = ImageDraw.Draw(im)

draw.line([(0, 0), (597, 0), (597, 597), (0, 597), (0, 0)], fill='black')
draw.rectangle((60, 90, 180, 180), fill='blue')
draw.ellipse((360, 90, 480, 180), fill='red')
draw.polygon(((171, 261), (237, 186), (282, 255), (360, 270), (309, 339)), fill='brown')
for i in range(100, 600, 2):
    draw.line([(i, 0), (600, i - 300)], fill='green')

draw.text((60, 450), 'Hello', fill='black')
fonts_folder = 'C:\\Windows\\Fonts'
BIG_SHOT_FONT = ImageFont.truetype(os.path.join(fonts_folder, 'big-shot.ttf'), 96)
draw.text((300, 450), 'Hello', fill='gray', font=BIG_SHOT_FONT)

im.save('drawing.png')