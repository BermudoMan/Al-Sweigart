from PIL import ImageColor, Image

print(ImageColor.getcolor('red', 'RGBA'))

cat_Im = Image.open('zophie.png')
print(cat_Im.size)
print(cat_Im.filename)
print(cat_Im.format)
print(cat_Im.format_description)
width, length = cat_Im.size
cat_Im.save('zophie.jpg')

im = Image.new('RGBA', (100, 200), 'purple')
im.save('purple_image.png')
im2 = Image.new('RGBA', (20, 20))
im2.save('transparent_image.png')

cat_Im = Image.open('zophie.jpg')
cropped_im = cat_Im.crop((335, 345, 565, 560))
cropped_im.save('cropped.png')