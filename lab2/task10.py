#!./venv/bin/python3

import matplotlib.pyplot as plt
from scipy.signal import convolve
import numpy as np


def main():
    a = [1, 4, 2]
    b = [1, 2, 3, 4, 5, 4, 3, 3, 2, 2, 1, 1]
    
    b1 = b[0:6]
    c1 = convolve(a, b1)
    
    b2 = b[6:12]
    c2 = convolve(a, b2)
    
    m = 14
    k = [i for i in range(1, m + 1)]

    c_add = np.concatenate((c1[0:6], c1[6:8] + c2[0:2], c2[2:]))

    plt.stem(k, list(c_add))
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.title('Convolution of a and b')
    plt.savefig('plots/task10.png')


if __name__ == "__main__":
    main()
