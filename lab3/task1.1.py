#!venv/bin/python3

import matplotlib.pyplot as plt
from math import sin, pi

def main():
    N = 64
    T = 1 / 128
    k = [i for i in range(0, N - 1)]
    f = [sin(2 * pi * 20 * i * T) for i in k]
    
    plt.plot(k, f)
    plt.grid()
    plt.xlabel('k')
    plt.ylabel('Y(t)')
    plt.title('Original signal')
    plt.savefig('plots/task1.1.png')


if __name__ == "__main__":
    main()
