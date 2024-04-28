#!venv/bin/python3

import matplotlib.pyplot as plt
from math import sin, pi
from scipy.fftpack import fft 
from numpy import unwrap, angle

def main():
    t = [i / 100 for i in range(0, 99)]
    x = [sin(2 * pi * 33 * i) + sin(2 * pi * 22 * i) for i in t]
    y = fft(x)
    m = [abs(i) for i in y]
    p = unwrap(angle(y))
    f = [i * (1 / (len(t) * (1 / 99))) for i in range(0, len(t))]

    plt.subplot(2, 1, 1)
    plt.plot(f, m)
    plt.title('Magnitude')
    plt.grid()
    plt.subplot(2, 1, 2)
    plt.plot(f, p * 180 / pi)
    plt.title('Phase')
    plt.grid()
    plt.savefig('plots/task2.1.2.png')


if __name__ == "__main__":
    main()
