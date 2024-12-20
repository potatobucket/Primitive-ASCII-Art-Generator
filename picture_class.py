import ascii_generator as ag
from PIL import Image, ImageFont, ImageDraw

def get_pixel_data(picture, mode = "L"):
    with Image.open(picture) as img:
        picWidth, picHeight = img.size[0], img.size[1]
        img = img.convert(mode)
        pixelData = [img.getpixel((column, row)) for row in range(picHeight) for column in range(picWidth)]
    return pixelData, picWidth, picHeight

class Picture:

    def __init__(self, image, fontSize = 20.0):
        self.imagePath = image
        with Image.open(image) as img:
            self.data, self.width, self.height = get_pixel_data(image)
        self.fontSize = fontSize
        self.fontWidth = (self.fontSize / 10.0) * 6
        self.fontHeight = (self.fontSize / 10.0) * 8.5
        self.font = ImageFont.truetype("cour", self.fontSize)
        self.widthWithFont = int(self.width * self.fontWidth)
        self.heightWithFont = int(self.height * self.fontHeight)
        self.characterData = [ag.assign_character(i) for i in self.data]
        self.asciiString = ag.make_string(self.characterData, self.width)

    def make_ascii_image(self, textColor = (0, 0, 0), bgColor = (255, 255, 255), save = False, savePath = "ascii_image.png"):
        newImage = Image.new("RGB", (self.widthWithFont, self.heightWithFont), bgColor)
        draw = ImageDraw.Draw(newImage)
        draw.text((0, 0), self.asciiString, font = self.font, fill = textColor, spacing = 0)
        newImage = newImage.resize((self.width * 12, self.height * 12))
        newImage.show()
        if save == True:
            newImage.save(savePath)
        newImage.close()

    def show_image(self):
        with Image.open(self.imagePath) as img:
            img.show()

    def __str__(self):
        return str(self.data)
