from PIL import Image
im = Image.open("foto.jpg")
print(im.format, im.size, im.mode)

w, h = im.size

out = im.resize((100, 100))


# out.show()

