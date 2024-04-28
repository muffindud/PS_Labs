#!venv/bin/python3

import matplotlib.pyplot as plt
from random import random
from math import pi
from scipy.signal import lfilter

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

    plt.plot(t, y1)
    plt.grid()
    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.title("White noise signal filtering")
    plt.savefig("plots/task4.2.png")


if __name__ == "__main__":
    main()
