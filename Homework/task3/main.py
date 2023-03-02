import math


def main(b, a, n, x):
    f = 0
    for c in range(1, n + 1):
        for j in range(1, a + 1):
            for k in range(1, b + 1):
                f += 9 * math.exp(c ** 2 + x ** 3 / 66) ** 6\
                     + 87 * k ** 3 + math.sin(j) ** 5
    return f
