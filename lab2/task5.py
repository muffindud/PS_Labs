#!./venv/bin/python3

import matplotlib.pyplot as plt
from scipy.signal import convolve
from numpy.fft import fft, ifft


def main():
    a = [-2, 0, 1, -1, 3]
    b = [1, 2, 0, -1]
    c = convolve(a, b)
    m = 8
    k = [i for i in range(1, m + 1)]

    AE = fft(a, m)
    BE = fft(b, m)
    p = AE * BE
    y1 = ifft(p, m)

    error = c - y1

    plt.stem(k, c, label='c')
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.title('a and b convolved')
    plt.savefig('plots/task5a.png')

    plt.clf()

    plt.stem(k, y1, label='y1')
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.title('IFFT of a * b')
    plt.savefig('plots/task5b.png')

    plt.clf()

    plt.stem(k, error, label='error')
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.title('Error')
    plt.savefig('plots/task5c.png')


if __name__ == "__main__":
    main()
