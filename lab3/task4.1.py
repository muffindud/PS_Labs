#!venv/bin/python3

import matplotlib.pyplot as plt
import random

def main():
    Ts = 0.01
    T = 50
    t = [i * Ts for i in range(0, int(T / Ts))]
    x1 = [random.random() for _ in range(len(t))]

    plt.plot(t, x1, linewidth=0.1)
    plt.grid()
    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.title("White noise signal")
    plt.savefig("plots/task4.1.png")


if __name__ == "__main__":
    main()
