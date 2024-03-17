import matplotlib.pyplot as plt


def main():
    R = 50
    m = [i for i in range(0, R - 1)]
    s = [2 * i * 0.9 ** i for i in m]

    plt.stem(m, s)
    plt.grid()
    plt.title("Original Signal")
    plt.xlabel("Time index")
    plt.ylabel("Amplitude")
    plt.savefig("plots/task2.1.png")


if __name__ == "__main__":
    main()
