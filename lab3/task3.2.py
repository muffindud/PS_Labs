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
    Fmax = 1 / Ts
    f = [i * Fmax for i in range(0, Fmax)]
    y = np.fft.fft(x)

    plt.stem(t, np.abs(y))
    
    plt.savefig("plots/task3.1.png")


if __name__ == "__main__":
    main()
