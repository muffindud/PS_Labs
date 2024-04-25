#!venv/bin/python3

import matplotlib.pyplot as plt
from math import sin, pi
from scipy.fftpack import fft

def main():
    N = 64
    T = 1 / 128
    k = [i for i in range(0, N - 1)]
    f = [sin(2 * pi * 20 * i * T) for i in k]
    F = fft(f)

    plt.plot(k, abs(F))
    plt.grid()
    plt.xlabel('k')
    plt.ylabel('Y(t)')
    plt.title('FFT of the original signal')
    plt.savefig('plots/task1.2.png')


if __name__ == "__main__":
    main()
