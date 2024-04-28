#!venv/bin/python3

import matplotlib.pyplot as plt
from random import random
from math import pi
from scipy.signal import lfilter
from scipy.fftpack import fft, fftshift


def main():
    om0 = 2 * pi
    dz = 0.05
    A = 1
    Ts = 0.01
    T = 50
    t = [i * Ts for i in range(0, int(T / Ts))]
    x1 = [random() for _ in range(len(t))]
    oms = om0 * Ts
    a = [1 + 2 * dz * oms + oms ** 2, -2 * (1 + dz * oms), 1]
    b = [A * 2 * dz * oms ** 2]
    y1 = lfilter(b, a, x1)
    df = 1 / T
    Fmax = 1 / (2 * Ts)
    f = [-Fmax / 2 + i * df for i in range(0, int(Fmax / df))]
    Fu1 = fft(x1)
    Fu2 = fft(y1)
    Fu1p = fftshift(Fu1)
    Fu2p = fftshift(Fu2)

    plt.stem(f, abs(Fu1p), markerfmt='r ', linefmt='r')
    plt.stem(f, abs(Fu2p), markerfmt='b ', linefmt='b')
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.title("White noise signal and its filtered version")
    plt.savefig("plots/task4.3.png")


if __name__ == "__main__":
    main()
