#!venv/bin/python3

import matplotlib.pyplot as plt
import numpy as np

def main():
    A = 0.75
    w = 0.5
    Ts = 0.01
    T = 100
    t = [i * Ts for i in range(0, int(T / Ts))]
    x = A * np.where(np.abs(t) <= w / 2, 1, 0)
    df = 1 / T
    Fmax = 1 / Ts
    f = [i * df for i in range(0, int(Fmax / df))]
    y = np.fft.fft(x)

    plt.stem(t, np.abs(y))
    plt.xlabel("Time")
    plt.ylabel("Magnitude")
    plt.title("Modulus of the Fourier transform of the discrete signal")
    plt.savefig("plots/task3.2.2.png")


if __name__ == "__main__":
    main()
