import matplotlib.pyplot as plt
import random


def main():
    R = 50
    m = [i for i in range(0, R - 1)]
    d = [random.random() - 0.5 for _ in range(len(m))]

    plt.stem(m, d)
    plt.grid()
    plt.title("Noise Signal")
    plt.xlabel("Time index")
    plt.ylabel("Amplitude")
    plt.savefig("plots/task2.2.png")


if __name__ == "__main__":
    main()
