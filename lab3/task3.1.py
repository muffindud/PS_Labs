#!venv/bin/python3

import matplotlib.pyplot as plt
import numpy as np

def main():
    A = 0.75
    w = 50
    Ts = 0.01
    T = 100
    t = [i * Ts for i in range(0, int(T / Ts))]
    x = A * np.where(np.abs(t) <= w / 2, 1, 0)

    plt.stem(t, x)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("Discrete signal")
    plt.savefig("plots/task3.1.png")


if __name__ == "__main__":
    main()
