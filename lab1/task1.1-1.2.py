import matplotlib.pyplot as plt
import random


def main():
    Ts = 0.01
    t = [round(i * Ts, 2) for i in range(int(5 / Ts))]
    x1 = [random.random() for _ in range(len(t))]

    plt.plot(t, x1, linewidth=0.75)
    plt.grid()
    plt.title("Random Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.savefig("plots/task1.1.png")

    plt.clf()

    t = [round(i * Ts, 2) for i in range(int(1 / Ts))]
    plt.hist(x1, t)
    plt.grid()
    plt.title("Random Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.savefig("plots/task1.2.png")


if __name__ == "__main__":
    main()
