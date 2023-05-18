import math


def main(n):
    if n == 0:
        return -0.02
    elif n >= 1:
        return (main(n - 1) - 57 * main(n - 1) ** 2 - main(n - 1) ** 3
                / 68) ** 2 + math.atan(main(n - 1)) ** 3 + main(n - 1)
    else:
        return 0


print(main(2))
print(main(5))
print(main(1))
print(main(8))
print(main(6))
