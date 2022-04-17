import math
import numpy as np

def printSinTable():
    x = np.arange(0, 2 * math.pi, math.pi / 500)
    for i in x:
        print('{0:.6f}\t{1:.6f}'.format(i, math.sin(i)))

def main():
    printSinTable()


if __name__=="__main__":
  main()