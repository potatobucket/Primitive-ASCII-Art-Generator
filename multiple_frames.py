import concurrent.futures
import os
import picture_class

def resize_and_convert_to_ascii(picture: str):
    """
Resizes the picture at the given path and converts it to an ASCII image.
    """
        
    frame: str = picture.split("\\")[-1]

    picture_class.resize_image(picture, 1080, 20)

    newFrame: picture_class.Picture = picture_class.Picture(picture)
    newFrame.make_ascii_image_color(save = True, savePath = f"Converted Frames\\{frame}")
    return f"Frame's done!"

def multiprocess_render(sourceFolder: str):
    """
Converts an entire folder's worth of images to ASCII using multiprocessing. It's remarkably faster.
    """

    if not os.path.isdir("Converted Frames"):
        os.makedirs("Converted Frames")

    frames: list = [f"{sourceFolder}\\{frame}" for frame in os.listdir(sourceFolder)]
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(resize_and_convert_to_ascii, frames, chunksize = 5)
    
        for result in results:
            print(result)

if __name__ == "__main__":
    userInput: str = input("Which folder?")

    multiprocess_render(userInput)
