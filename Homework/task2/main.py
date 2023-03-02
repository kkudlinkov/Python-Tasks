import math


def main(x):
    f = 0
    if x < 92:
        f = 1 - 61 * pow(math.ceil(x), 7) - pow(1 + pow(x, 3) / 23, 4) / 47
    elif 92 <= x < 143:
        f = 0.04 - 91 * math.pow(math.cos(x), 7)
    elif 143 <= x < 189:
        f = 6 * math.pow(x, 6) + math.pow(x, 2) + 85 * math.pow(x, 2)
    elif x >= 189:
        f = math.pow(1 + 52 * math.pow(x, 3) + 49 * math.pow(x, 2),
                     7) - 4 * math.pow(62 * math.pow(x, 3), 3)
    return f
