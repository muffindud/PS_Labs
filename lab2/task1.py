#!./venv/bin/python3

import matplotlib.pyplot as plt


def main():
    a = [-2, 0, 1, -1, 3]
    b = [1, 2, 0, -1]
    d = 5
    n = [i for i in range(1, 1, d)]
    c = 4
    l = [i for i in range(1, 1, c)]

    plt.subplot(2, 1, 1)
    plt.stem(n, a)
    plt.title('Sequence a')
    plt.xlabel('Time index n')
    plt.ylabel('Amplitude')

    plt.subplot(2, 1, 2)
    plt.stem(l, b)
    plt.xlabel('Time index n')
    plt.ylabel('Amplitude')
    plt.title('Sequence b')

    plt.savefig('plots/task1.png')



if __name__ == "__main__":
    main()
