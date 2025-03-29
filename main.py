import picture_class as pc

#-- With the Picture class the most code that should be needed is this:
if __name__ == "__main__":
    picturePath: str = input("Please enter path to picture. >")
    picture = pc.Picture(picturePath, fontSize = 10.0)
    color: str = input("(M)onochrome or (C)olor? >").lower()
    if color == "m" or color == "monchrome":
        picture.make_ascii_image_monochrome(textColor = (255, 255, 255), bgColor = (0, 0, 0), save = True)
    elif color == "c" or color == "color":
        picture.make_ascii_image_color(save = True)

    #-- although you could also just call "make_ascii_image" directly like so:
    #-- pc.Picture("your picture here.png").make_ascii_image(save = True)
