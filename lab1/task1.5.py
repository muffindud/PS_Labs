import matplotlib.pyplot as plt
import random
from math import pi
from scipy.signal import lfilter


def main():
    Ts = 0.01
    om0 = 2 * pi
    dz = 0.005
    A = 1
    oms = om0 * Ts
    a = [
        1 + 2 * dz * oms + oms ** 2,
        -2 * (1 + dz * oms),
        1
    ]
    b = [
        A * 2 * oms ** 2
    ]
    t = [round(i * Ts, 2) for i in range(int(50 / Ts))]
    x1 = [random.random() for _ in range(len(t))]
    y1 = list(lfilter(b, a, x1))
    

    plt.plot(t, y1, linewidth=0.75)
    plt.grid()
    plt.title("Noise filtering with a 2nd order filter")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.savefig("plots/task1.5.png")


if __name__ == "__main__":
    main()
