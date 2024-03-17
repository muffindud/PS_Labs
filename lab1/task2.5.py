import matplotlib.pyplot as plt
import random
from scipy.signal import lfilter


def main():
    R = 50
    m = [i for i in range(0, R - 1)]
    s = [2 * i * 0.9 ** i for i in m]
    d = [random.random() - 0.5 + s[i] for i in range(len(m))]
    M = 3
    b = [1 / M for _ in range(M)]
    y = lfilter(b, 1, d)

    plt.plot(m, s, linewidth=1, label="Original Signal")
    plt.plot(m, d, linewidth=1, label="Noisy Signal")
    plt.plot(m, y, linewidth=1, label="Filtered Signal")
    plt.legend()
    plt.grid()
    plt.title("MAF Filtered Signal")
    plt.xlabel("Time index")
    plt.ylabel("Amplitude")
    plt.savefig("plots/task2.5.png")


if __name__ == "__main__":
    main()
