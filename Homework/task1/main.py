import math


def main(x):
    n = math.pow(x, 5) / 47 - math.pow(x, 6)
    d = math.pow(math.sin(x - 20 * math.pow(x, 2) - 59 * math.pow(x, 3)),
                 6) / 96 - math.pow(x, 7)
    return math.pow(x, 8) + n / d
