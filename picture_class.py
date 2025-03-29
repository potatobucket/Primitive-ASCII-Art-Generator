"""
Holds the Picture class which contains all the logic for automatically generating a .png of an ASCII image of a given picture.
"""

import ascii_generator as ag
from PIL import Image, ImageFont, ImageDraw, ImageChops

def add_color(firstImage: str, secondImage: str):
    """
    Uses the second image as a mask to add the first image's colors to it.
    """
    with Image.open(firstImage) as base:
        with Image.open(secondImage) as mask:
            mask = mask.convert("RGB")
            base = base.convert("RGB").resize(mask.size)
            ImageChops.add(base, mask).save("test_color.png")

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

def resize_image(imagePath: str, finalSize: int, fontWidth: int):
    """
    WARNING: This overwrites the original picture. If you want to keep a full-size version of your picture make a copy!\n
    Resizes an image so that when run through the ASCII generator it comes out at the final size.
    """
    with Image.open(imagePath) as img:
        width, height = img.size
        aspectRatio: float = width / height
        newWidth: int = int(finalSize / fontWidth)
        newHeight: int = int((finalSize / aspectRatio) / fontWidth)
        img = img.resize((int(newWidth), int(newHeight)))
        img.save(imagePath)
        return imagePath

class Picture:
    """
    A class to hold a picture and handles all the malarky of turning it into an ASCII image.
    """

    def __init__(self, image: str, finalImageSize: int = 1080, fontSize: float = 20.0):
        self.imagePath: str = image
        resize_image(self.imagePath, finalImageSize, fontSize)
        with Image.open(image) as img:
            img = img.convert("RGB")
            self.data, self.width, self.height = get_pixel_data(image)
            self.pixelColors: Image.PixelAccess = img.load()
        self.fontSize: float = fontSize
        self.fontWidth: float = (self.fontSize / 10.0) * 6
        self.fontHeight: float = (self.fontSize / 10.0) * 8.5
        self.font: ImageFont = ImageFont.truetype("courbd", self.fontSize, encoding = "utf-8")
        self.widthWithFont: int = int(self.width * self.fontWidth)
        self.heightWithFont: int = int(self.height * self.fontHeight)
        self.characterData: list[str] = [ag.assign_character(i) for i in self.data]
        self.asciiString: str = ag.make_string(self.characterData, self.width)

    def make_ascii_image_color(self, bgColor: tuple[int] = (0, 0, 0), save: bool = False, show: bool = False, savePath: str = "ascii_image_color.png"):
        """
        Creates a color ASCII image of the Picture.

        Parameters:
        bgColor: the color of the background as a tuple of (R, G, B) values
        save: whether or not to save the generated image
        show: whether or not to show the generated image in your computer's default image viewer
        savePath: what name to save the generated image as
        """

        with Image.open(self.imagePath) as img:
            index: int = 0
            newImage: Image = Image.new("RGB", (int(self.fontWidth) * self.width, int(self.fontHeight) * self.height), bgColor)
            draw: ImageDraw = ImageDraw.Draw(newImage)

            for i in range(self.height):
                for j in range(self.width):
                    draw.text((j * self.fontWidth, i * self.fontHeight), ag.assign_character(self.data[index]), font = self.font, fill = self.pixelColors[j, i])
                    index += 1
            
            newImage = newImage.resize((self.width * int(self.fontWidth), self.height * int(self.fontWidth)))

            if show == True:
                newImage.show()
            if save == True:
                newImage.save(savePath)
            newImage.close()

    def make_ascii_image_monochrome(self, textColor: tuple[int] = (0, 0, 0), bgColor: tuple[int] = (255, 255, 255), save: bool = False, show: bool = False, savePath: str = "ascii_image_monochrome.png"):
        """
        Creates a monochrome ASCII image of the Picture.

        Parameters:
        textColor: the color of the text as a tuple of (R, G, B) values
        bgColor: the color of the background as a tuple of (R, G, B) values
        save: whether or not to save the generated image
        show: whether or not to show the generated image in your computer's default image viewer
        savePath: what name to save the generated image as
        """
        newImage: Image = Image.new("RGB", (self.widthWithFont, self.heightWithFont), bgColor)
        draw: ImageDraw = ImageDraw.Draw(newImage)
        draw.text((0, 0), self.asciiString, font = self.font, fill = textColor, spacing = 0)
        newImage = newImage.resize((self.width * int(self.fontWidth), self.height * int(self.fontWidth)))
        if show == True:
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
