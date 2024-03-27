#!./venv/bin/python3

import matplotlib.pyplot as plt
from scipy.signal import convolve


def main():
    a = [1, 4, 2]
    b = [1, 2, 3, 4, 5, 4, 3, 3, 2, 2, 1, 1]
    
    b1 = b[0:6]
    c1 = convolve(a, b1)
    
    b2 = b[6:12]
    c2 = convolve(a, b2)
    
    m = 8
    k = [i for i in range(1, m + 1)]

    plt.stem(k, c1)
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.title('Convolution of a and b1')
    plt.savefig('plots/task9a.png')

    plt.clf()

    plt.stem(k, c2)
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.title('Convolution of a and b2')
    plt.savefig('plots/task9b.png')


if __name__ == "__main__":
    main()
