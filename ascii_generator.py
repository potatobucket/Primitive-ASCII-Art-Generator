import math
import numpy as np

def assign_character(value):
    densityMap = "Ñ@#W$9876543210?!abc;:+=-,._ "
    #densityMap = "█▓▒░▪▫ "
    return densityMap[math.floor(np.interp(value, [0, 256], [0, len(densityMap)]))]

if __name__ == "__main__":
    for i in range(256):
        print(i, " = ", assign_character(i))
