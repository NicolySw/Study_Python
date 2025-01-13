from PIL import Image, ImageDraw, ImageFont


class PostMaker:
    def __init__(self, name_photo):
        self.image = Image.open(name_photo)
        self.w, self.h = self.image.size
        self.image = self.image.resize((self.w // 2, self.h // 2))

    def paste(self, name_photo):
        pastel_image = Image.open(name_photo)
        pastel_image = pastel_image.resize((pastel_image.size[0] // 2, pastel_image.size[1] // 2))
        self.image.paste(pastel_image, (10, 10))

    def upgrade(self, text):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype('arial.ttf', 30)
        draw.text((10, 10), text, font=font)
        self.image.show()


image = PostMaker('foto.jpg')
image.paste('foto2.png')
image.upgrade('Привет')
