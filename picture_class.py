from PIL import Image, ImageFont

def get_pixel_data(picture, mode = "L"):
    with Image.open(picture) as img:
        picWidth, picHeight = img.size[0], img.size[1]
        img = img.convert(mode)
        pixelData = [img.getpixel((column, row)) for row in range(picHeight) for column in range(picWidth)]
    return pixelData, picWidth, picHeight

class Picture:

    def __init__(self, image):
        self.imagePath = image
        with Image.open(image) as img:
            self.data, self.width, self.height = get_pixel_data(image)
        self.font = ImageFont.truetype("cour", 20.0)
        self.widthWithFont = self.width * 12
        self.heightWithFont = self.height * 17

    def show_image(self):
        with Image.open(self.imagePath) as img:
            img.show()

    def __str__(self):
        return str(self.data)
