import matplotlib.pyplot as plt
import random


def main():
    R = 50
    m = [i for i in range(0, R - 1)]
    s = [2 * i * 0.9 ** i for i in m]
    d = [random.random() - 0.5 for _ in range(len(m))]

    plt.plot(m, s, linewidth=1, label="Original Signal")
    plt.plot(m, d, linewidth=1, label="Noise Signal")
    plt.grid()
    plt.title("Original Signal")
    plt.xlabel("Time index")
    plt.ylabel("Amplitude")
    plt.savefig("plots/task2.3.png")


if __name__ == "__main__":
    main()
