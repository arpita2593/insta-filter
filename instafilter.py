#import image from PIL
from PIL import Image
#load images into objects
base_img = Image.open("2.jpg")
img_filter = Image.open("filter5.jpg")
third = Image.open("1.jpg")
#set o\p image size
size = (760,760)
#resize all images
base_img=base_img.resize(size)
img_filter=img_filter.resize(size)

#split each image
r,g,b = base_img.split()
R,G,B = img_filter.split()

#merge
im = Image.merge("RGB",(R,g,B))
im.show()