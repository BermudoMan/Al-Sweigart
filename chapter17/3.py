# image size changing
from PIL import Image

cat_im = Image.open('zophie.png')
width, height = cat_im.size
quartersized_im = cat_im.resize((int(width/2), int(height/2)))
quartersized_im.save('quartersized.png')
svelte_im = cat_im.resize((width, height + 300))
svelte_im.save('svelte.png')

# rotating and flipping

cat_im.rotate(45).save('rotated45.png')
cat_im.rotate(45, expand=True).save('rotated45_expanded.png')

cat_im.transpose(Image.FLIP_LEFT_RIGHT).save('horiz_flip.png')