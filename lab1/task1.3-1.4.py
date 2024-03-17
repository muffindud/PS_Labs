import matplotlib.pyplot as plt
import random


def main():
    Ts = 0.001
    t = [round(i * Ts, 3) for i in range(int(5 / Ts))]
    x2 = [random.random() for _ in range(len(t))]

    plt.plot(t, x2, linewidth=0.25)
    plt.grid()
    plt.title("Random Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.savefig("plots/task1.3.png")

    plt.clf()

    t = [round(i * Ts, 3) for i in range(int(1 / Ts))]
    plt.hist(x2, t)
    plt.grid()
    plt.title("Random Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.savefig("plots/task1.4.png")


if __name__ == "__main__":
    main()
