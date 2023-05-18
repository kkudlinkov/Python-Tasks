import math


def main(n, a, m, p):
    pr = 1
    f = 0
    for c in range(1, m + 1):
        for k in range(1, a + 1):
            for j in range(1, n + 1):
                f += 63 * (c ** 3 - 0.02 - 43 * j) ** 5 + 76 * k ** 2 - 1 - p
                print(f)
        pr *= f

    return pr


print(main(8, 5, 8, -0.45))
