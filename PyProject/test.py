from PIL import Image 

im = Image.open("vizitka.png")
im_rotate = im.rotate(90)
im_rotate.save('vizitka.png', quality=95)
im.close()
