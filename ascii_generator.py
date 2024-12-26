"""
Handles the generation of an ASCII representation of a given picture.
"""

import math
import numpy as np

def assign_character(value: int | float): #-- possible update: make all of this make sense
    """
    Assigns an ASCII character roughly translating to the value intensity of black in a pixel.\n
    i.e. a fully black pixel would be Ñ and a fully white pixel would be " " (a space)
    """
    #densityMap: str = "ÑÑÑÑ@#W$9876543210?!abc;:+=-…,._ "[::-1]
    #densityMap: str = "█▓▒░▪▫ "#[::-1]
    densityMap: str = "Ñ@QB#NgWM8RDHdOKq9$6khEPXwmeZaoS2yjufF]}{tx1zv7lciL/\\|?*>r^;:_\"~…,'.-` "[::-1]
    #densityMap: str = "█▉▇▓▊▆▅▌▚▞▀▒▐▍▃▖▂░▁▏"#[::-1]
    #densityMap: str = "█▉▇▓▊▆▅▌▚▞▀▒▐▃▂░▁"#[::-1]
    #densityMap: str = "◙◘■▩●▦▣◚◛◕▨▧◉▤◐◒▮◍◑▼▪◤▬◗◭◖◈◎◮◊◫▰◄◯□▯▷▫▽◹△◁▸▭◅▵◌▱▹▿◠◃◦◟◞◜ "[::-1]
    #densityMap: str = "╬╠╫╋║╉╩┣╦╂╳╇╈┠╚┃╃┻╅┳┡┢┹╀╧┱╙┗┞┇┸┋┯┰┖╲╱┎╘━┭┕┍┅╾│┬┉╰╭╸└┆╺┊─╌┄┈╴╶  "[::-1]
    #densityMap: str = "ぽぼゑぜぬあおゆぎゐはせぢがきぱびほげばゟぁたかぞぷれひずどらさでけぉちごえすゎにづぇとょついこぐうぅぃくっしへゞゝ゚゙ "[::-1]
    return densityMap[math.floor(np.interp(value, [0, 256], [0, len(densityMap)]))]

def make_string(data: list[str], width: int):
    """
    Combines all the elements of a list of strings together to make one big string with line returns matching the desired width of the product.
    """
    newString: str = ""
    for index,datum in enumerate(data):
        if (index + 1) % width == 0:
            newString += f"{datum}\n"
        else:
            newString += f"{datum}"
    return newString

def create_txt_file(data: list[str], width: int, filename: str):
    """
    Creates a .txt file containing the string generated by the given data.
    """
    with open(f"{filename}.txt", "w", encoding = "utf-8") as textFile:
        textFile.write(make_string(data, width))
