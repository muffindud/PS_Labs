#!./venv/bin/python3

import matplotlib.pyplot as plt
from scipy.signal import convolve

def main():
    a = [-2, 0, 1, -1, 3]
    b = [1, 2, 0, -1]
    d = 5
    c = convolve(a, b)
    k = [i for i in range(1, 8 + 1)]

    plt.stem(k, c)
    plt.title('a and b convolved')
    plt.xlabel('Time index')
    plt.ylabel('Amplitude')
    plt.savefig('plots/task2.png')



if __name__ == "__main__":
    main()
