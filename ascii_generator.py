import math
import numpy as np

def assign_character(value):
    #densityMap = "Ñ@#W$9876543210?!abc;:+=-,._ "
    #densityMap = "█▓▒░▪▫ "
    #densityMap = "@QB#NgWM8RDHdOKq9$6khEPXwmeZaoS2yjufF]}{tx1zv7lciL/\\|?*>r^;:_\"~,'.-` "
    densityMap = "█▉▇▓▊▆▅▌▚▞▀▒▐▍▃▖▂░▁▏ "
    #densityMap = "◙◘■▩●▦▣◚◛◕▨▧◉▤◐◒▮◍◑▼▪◤▬◗◭◖◈◎◮◊◫▰◄◯□▯▷▫▽◹△◁▸▭◅▵◌▱▹▿◠◃◦◟◞◜ "
    #densityMap = "╬╠╫╋║╉╩┣╦╂╳╇╈┠╚┃╃┻╅┳┡┢┹╀╧┱╙┗┞┇┸┋┯┰┖╲╱┎╘━┭┕┍┅╾│┬┉╰╭╸└┆╺┊─╌┄┈╴╶  "
    #densityMap = "ぽぼゑぜぬあおゆぎゐはせぢがきぱびほげばゟぁたかぞぷれひずどらさでけぉちごえすゎにづぇとょついこぐうぅぃくっしへゞゝ゚゙ "
    return densityMap[math.floor(np.interp(value, [0, 256], [0, len(densityMap)]))]

def make_string(data, width):
    newString = ""
    for index,datum in enumerate(data):
        if (index + 1) % width == 0:
            newString += f"{datum}\n"
        else:
            newString += f"{datum}"
    return newString

if __name__ == "__main__":
    for i in range(256):
        print(i, " = ", assign_character(i))
