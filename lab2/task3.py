#!./venv/bin/python3

import matplotlib.pyplot as plt
from numpy.fft import fft, ifft


def main():
    a = [-2, 0, 1, -1, 3]
    b = [1, 2, 0, -1]
    m = 8
    k = [i for i in range(1, m + 1)]
    AE = fft(a, m)
    BE = fft(b, m)
    p = AE * BE

    plt.stem(k, p)
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.title('FFT of a * b')
    plt.savefig('plots/task3.png')


if __name__ == "__main__":
    main()
