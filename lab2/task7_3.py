#!./venv/bin/python3

import matplotlib.pyplot as plt
from numpy import pi
from numpy.fft import fft, ifft
from scipy.signal import sawtooth, square, convolve
from timeit import default_timer


def main():
    d = 262144
    n = [i for i in range(1, d + 1)]
    a = 2.6 * square([28 * pi * i + 1 for i in n])

    c = 262144
    l = [i for i in range(1, c + 1)]
    b = 3.8 * sawtooth([22 * pi * i + 1 for i in l])

    m = d + c

    start = default_timer()
    AE = fft(a, m)
    BE = fft(b, m)
    p = AE * BE
    y1 = ifft(p, m)
    end = default_timer()

    print(f"FFT time: {end - start}")


if __name__ == "__main__":
    main()
