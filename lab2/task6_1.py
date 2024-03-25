#!./venv/bin/python3

import matplotlib.pyplot as plt
from numpy import pi
from numpy.fft import fft, ifft
from scipy.signal import sawtooth, square, convolve


def main():
    d = 65536
    n = [i for i in range(1, d + 1)]
    a = 2.6 * square([28 * pi * i + 1 for i in n])
    
    c = 65536
    l = [i for i in range(1, c + 1)]
    b = 3.8 * sawtooth([22 * pi * i + 1 for i in l])

    m = d + c
    k = [i for i in range(1, m + 1)]

    plt.stem(n, a)
    plt.xlabel('Time index')
    plt.ylabel('Amplitude')
    plt.title('Signal a')
    plt.savefig('plots/task6.1a.png')

    plt.clf()

    plt.stem(l, b)
    plt.xlabel('Time index')
    plt.ylabel('Amplitude')
    plt.title('Signal b')
    plt.savefig('plots/task6.1b.png')

    plt.clf()

    c = convolve(a, b)

    plt.stem(k[0:-1], c)
    plt.title('a and b convolved')
    plt.xlabel('Time index')
    plt.ylabel('Amplitude')
    plt.savefig('plots/task6.1c.png')

    plt.clf()

    AE = fft(a, m)
    BE = fft(b, m)
    p = AE * BE
    
    plt.stem(k, p)
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.title('FFT of a * b')
    plt.savefig('plots/task6.1d.png')

    plt.clf()

    y1 = ifft(p, m)

    plt.stem(k, y1)
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.title('IFFT of a * b')
    plt.savefig('plots/task6.1e.png')


if __name__ == "__main__":
    main()
