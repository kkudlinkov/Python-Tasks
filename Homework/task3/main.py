import math


def main(n):
    if n == 0:
        return 0.16
    elif n == 1:
        return 0.96
    elif n >= 2:
        return 1 - math.pow(main(n - 1), 4) - main(n - 2)
    else:
        return 0
