import matplotlib.pyplot as plt
import random
from scipy.signal import lfilter


def main():
    R = 50
    m = [i for i in range(0, R - 1)]
    s = [2 * i * 0.9 ** i for i in m]
    d = [random.random() - 0.5 + s[i] for i in range(len(m))]
    M0 = 3
    b0 = [1 / M0 for _ in range(M0)]
    y0 = lfilter(b0, 1, d)
    M1 = 5
    b1 = [1 / M1 for _ in range(M1)]
    y1 = lfilter(b1, 1, d)
    M2 = 10
    b2 = [1 / M2 for _ in range(M2)]
    y2 = lfilter(b2, 1, d)

    plt.plot(m, s, linewidth=1, label="Original Signal")
    plt.plot(m, d, linewidth=1, label="Noisy Signal")
    plt.plot(m, y0, linewidth=1, label="M=3 Filtered Signal")
    plt.plot(m, y1, linewidth=1, label="M=5 Filtered Signal")
    plt.plot(m, y2, linewidth=1, label="M=10 Filtered Signal")
    plt.legend()
    plt.grid()
    plt.title("MAF Filtered Signal")
    plt.xlabel("Time index")
    plt.ylabel("Amplitude")
    plt.savefig("plots/task2.6.png")


if __name__ == "__main__":
    main()
