import math


def sum(b, a, n, x):
    f = 0
    for c in range(1, n + 1):
        for j in range(1, a + 1):
            for k in range(1, b + 1):
                f += 9 * math.exp(6) * (math.pow(c, 2) + math.pow(x, 3) / 66) + 87 * math.pow(k, 3) + math.pow(
                    math.sin(j), 5)
    return f


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(sum(6, 5, 7, -0.04))
