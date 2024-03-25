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
    y1 = ifft(p, m)

    plt.stem(k, y1)
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.title('IFFT of a * b')
    plt.savefig('plots/task4.png')


if __name__ == "__main__":
    main()
