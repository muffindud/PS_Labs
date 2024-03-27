#!./venv/bin/python3

import matplotlib.pyplot as plt
from numpy.fft import ifft
from numpy import array


def main():
    d = 8
    n = [i for i in range(1, d + 1)]
    a = [6, 8, 7, 3, 0, 0, 0, 0]

    c = 8
    l = [i for i in range(1, c + 1)]
    b = [4, 9, 3, 1, 1, 0, 0, 0]

    ms = array(a) * array(b) 
    ims = ifft(ms).real

    print(ims)

if __name__ == "__main__":
    main()
