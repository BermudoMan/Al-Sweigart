# logo adding
#! python3 
# project1 - resize of all images in directory to 300x300 dimentions and add logo

import os
from PIL import Image

# constants
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logo_im = Image.open(LOGO_FILENAME)
print(logo_im.size)
w, h = logo_im.size
logo_im2 = logo_im.resize((int(w/6), int(h/6)))
logo_width, logo_height = logo_im2.size
print(logo_im2.size)

os.makedirs('with_logo', exist_ok=True)
# cycle for all files in the dir
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
            or filename == LOGO_FILENAME:
        continue # skip logo and another file types

    im = Image.open(filename)
    width, height = im.size

# resize images in dir
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
            print('Resizing image dimantions %s...' % (filename))    
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
            print('Resizing image dimantions %s...' % (filename))    
            im = im.resize((width, height))

# logo adding
        print('logo adding to the image %s...' % (filename))
        im.paste(logo_im2, (width - logo_width, height - logo_height), logo_im2)
        im.save(os.path.join('with_logo', filename))
