from PIL import Image, ImageDraw, ImageFont


def new_photo(name):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w//2, h//2))


im = new_photo('foto.jpg')
im_2 = new_photo('foto2.png')

w, h = im.size
im.paste(im_2, (w-100, h-100))
draw = ImageDraw.Draw(im)
font = ImageFont.truetype('arial.ttf', 50)
draw.text((0, 0), text='Hello World', font=font, fill='red')
im.show('MyPhoto')

