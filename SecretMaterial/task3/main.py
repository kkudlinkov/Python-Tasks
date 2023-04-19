import math


def main(n, a, m, p):
    ans = 0
    k = 1
    for c in range(1, m + 1):
        s = 0
        for k in range(1, a + 1):
            for j in range(1, n + 1):
                s += 63 * (c ** 3 - 0.02 - 43 * j) ** 5 + 76 * pow(k, 2) - 1 - p
        k *= s
    ans += k
    return ans


print(main(8, 5, 8, -0.45))
print(main(6, 4, 7, -0.46))
