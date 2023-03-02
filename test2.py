import math


def f(n):
    if n == 0:
        return 0.16
    elif n == 1:
        return 0.96
    elif n >= 2:
        return 1 - math.pow(f(n - 1), 4) - f(n - 2)
    else:
        return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f(5))
