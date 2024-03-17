import matplotlib.pyplot as plt
import random
from scipy.signal import lfilter, sawtooth
from math import pi


def main():
    R = 1
    m = [round(i * 0.001, 3) for i in range(0, R * 1000)]
    s = [2 * sawtooth(3 * pi * i + pi / 6) for i in m]
    d = [random.random() - 0.5 + i for i in s]
    M0 = 20
    b0 = [1 / M0 for _ in range(M0)]
    y0 = lfilter(b0, 1, d)

    plt.plot(m, s, linewidth=0.75, label="Original Signal")
    plt.plot(m, d, linewidth=0.75, label="Noisy Signal")
    plt.plot(m, y0, linewidth=0.75, label="M=20 Filtered Signal")
    plt.legend()
    plt.grid()
    plt.title("MAF Filtered Signal")
    plt.xlabel("Time index")
    plt.ylabel("Amplitude")
    plt.savefig("plots/task2.7.png")


if __name__ == "__main__":
    main()
