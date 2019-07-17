from PIL import Image

base_img = Image.open("2.jpg")
img_filter = Image.open("filter5.jpg")
third = Image.open("1.jpg")

size = (760,760)

base_img=base_img.resize(size)
img_filter=img_filter.resize(size)
third = third.resize(size)

r,g,b = base_img.split()
R,G,B = img_filter.split()
Rr,Gg,Bb = third.split()

im = Image.merge("RGB",(R,g,B))
im.show()