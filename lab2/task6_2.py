#!./venv/bin/python3

import matplotlib.pyplot as plt
from numpy import pi
from numpy.fft import fft, ifft
from scipy.signal import sawtooth, square, convolve
from timeit import default_timer


def main():
    d = 65536
    n = [i for i in range(1, d + 1)]
    a = 2.6 * square([28 * pi * i + 1 for i in n])
    
    c = 65536
    l = [i for i in range(1, c + 1)]
    b = 3.8 * sawtooth([22 * pi * i + 1 for i in l])

    m = d + c
    k = [i for i in range(1, m + 1)]

    start = default_timer()
    c = convolve(a, b)
    end = default_timer()

    print(f"Convolution time: {end - start}")


if __name__ == "__main__":
    main()
