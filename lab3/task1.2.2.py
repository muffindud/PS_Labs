#!venv/bin/python3

import matplotlib.pyplot as plt
from math import sin, pi
from scipy.fftpack import fft

def main():
    N = 64
    T1 = 1 / 94
    T2 = 1 / 74
    T3 = 1 / 54
    T4 = 1 / 34
    k = [i for i in range(0, N - 1)]
    f1 = [sin(2 * pi * 20 * i * T1) for i in k]
    F1 = fft(f1)
    f2 = [sin(2 * pi * 20 * i * T2) for i in k]
    F2 = fft(f2)
    f3 = [sin(2 * pi * 20 * i * T3) for i in k]
    F3 = fft(f3)
    f4 = [sin(2 * pi * 20 * i * T4) for i in k]
    F4 = fft(f4)

    plt.subplot(2, 1, 1)
    plt.plot(k, f1, color='red')
    plt.plot(k, f2, color='blue')
    plt.plot(k, f3, color='green')
    plt.plot(k, f4, color='yellow')
    plt.grid()
    plt.xlabel('k')
    plt.ylabel('Y(t)')
    plt.title('Original signals')
    plt.legend(['94 Hz', '74 Hz', '54 Hz', '34 Hz'])
    
    plt.subplot(2, 1, 2)
    plt.plot(k, abs(F1), color='red')
    plt.plot(k, abs(F2), color='blue')
    plt.plot(k, abs(F3), color='green')
    plt.plot(k, abs(F4), color='yellow')
    plt.grid()
    plt.xlabel('k')
    plt.ylabel('Y(t)')
    plt.title('FFT of the original signals')
    plt.legend(['94 Hz', '74 Hz', '54 Hz', '34 Hz'])

    plt.savefig('plots/task1.2.2.png')


if __name__ == "__main__":
    main()
