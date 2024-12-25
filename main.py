import picture_class as pc

#-- With the Picture class the most code that should be needed is this:
if __name__ == "__main__":
    picture = pc.Picture("Examples/basic_example.png")
    picture.make_ascii_image(save = True)

    #-- although you could also just call "make_ascii_image" directly like so:
    #-- pc.Picture("your picture here.png").make_ascii_image(save = True)
