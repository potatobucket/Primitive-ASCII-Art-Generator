"""
Holds the Picture class which contains all the logic for automatically generating a .png of an ASCII image of a given picture.
"""

import ascii_generator as ag
from PIL import Image, ImageFont, ImageDraw

def get_pixel_data(picture: str, mode: str = "L"):
    """
    Returns the values of each pixel in the given picture as well as its width and height in pixels.
    """
    with Image.open(picture) as img:
        picWidth: int = img.size[0]
        picHeight: int = img.size[1]
        img = img.convert(mode)
        pixelData: list[int] = [img.getpixel((column, row)) for row in range(picHeight) for column in range(picWidth)]
    return pixelData, picWidth, picHeight

class Picture:
    """
    A class to hold a picture and handles all the malarky of turning it into an ASCII image.
    """

    def __init__(self, image: str, fontSize: float = 20.0):
        self.imagePath: str = image
        with Image.open(image) as img:
            self.data, self.width, self.height = get_pixel_data(image)
        self.fontSize: float = fontSize
        self.fontWidth: float = (self.fontSize / 10.0) * 6
        self.fontHeight: float = (self.fontSize / 10.0) * 8.5
        self.font: ImageFont = ImageFont.truetype("cour", self.fontSize)
        self.widthWithFont: int = int(self.width * self.fontWidth)
        self.heightWithFont: int = int(self.height * self.fontHeight)
        self.characterData: list[str] = [ag.assign_character(i) for i in self.data]
        self.asciiString: str = ag.make_string(self.characterData, self.width)

    def make_ascii_image(self, textColor: tuple[int] = (0, 0, 0), bgColor: tuple[int] = (255, 255, 255), save: bool = False, savePath: str = "ascii_image.png"):
        """
        Creates an ASCII image of the Picture.

        Parameters:
        textColor: the color of the text as a tuple of (R, G, B) values
        bgColor: the color of the background as a tuple of (R, G, B) values
        save: whether or not to save the generated image
        savePath: what name to save the generated image as
        """
        newImage: Image = Image.new("RGB", (self.widthWithFont, self.heightWithFont), bgColor)
        draw: ImageDraw = ImageDraw.Draw(newImage)
        draw.text((0, 0), self.asciiString, font = self.font, fill = textColor, spacing = 0)
        newImage = newImage.resize((self.width * 12, self.height * 12))
        newImage.show()
        if save == True:
            newImage.save(savePath)
        newImage.close()

    def show_image(self):
        """
        Shows the original image.
        """
        with Image.open(self.imagePath) as img:
            img.show()

    def __repr__(self):
        return f"Picture(image = {self.imagePath}, fontSize = {self.fontSize})"

    def __str__(self):
        return str(self.data)
