#!venv/bin/python3

import matplotlib.pyplot as plt
from math import sin, pi
from scipy.fftpack import fft

def main():
    N = 64
    T = 1 / 128
    k = [i for i in range(0, N - 1)]
    hertz = [i * (1 / (N * T)) for i in k]
    f = [sin(2 * pi * 20 * i * T) for i in k]
    F = fft(f)
    magF = [abs(F[i]) for i in k]

    plt.plot(hertz[:N // 2], magF[:N // 2])
    plt.grid()
    plt.xlabel('k')
    plt.ylabel('Y(t)')
    plt.title('Half of the FFT of the original signal')
    plt.savefig('plots/task1.3.png')


if __name__ == "__main__":
    main()
