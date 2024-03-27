#!./venv/bin/python3

import matplotlib.pyplot as plt
from scipy.signal import convolve


def main():
    a = [1, 4, 2]
    b = [1, 2, 3, 4, 5, 4, 3, 3, 2, 2, 1, 1]
    c = convolve(a, b)
    m = 14
    k = [i for i in range(1, m + 1)]

    plt.stem(k, c)
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.title('Convolution of a and b')
    plt.savefig('plots/task8.png')


if __name__ == "__main__":
    main()
