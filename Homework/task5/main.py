import math


def main(x):
    s = 0
    for i in range(1, len(x) + 1):
        s += 81 * (70 * x[math.ceil(i / 3) - 1] + 1 + 39 *
                   x[len(x) + 1 - math.ceil(i / 3) - 1] ** 2) ** 2
    return 84 * s