
import numpy as np
import matplotlib.pyplot as plt


def pathReader():
    count = 0
    path = []
    with open("path.txt") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('#'):
                pass
            else:
                if count == 0:
                    count += 1
                elif count >= 1:
                    split = line.split(' ')
                    x = int(split[0])
                    y = int(split[1])
                    pos = [x, y]
                    path.append(pos)
                    
    array = np.array(path)
    #print(array)
    return array

pathReader()