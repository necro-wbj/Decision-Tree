#! python3
import math


def entropy(m, n):
    return -m * math.log(m, 2) - n * math.log(n, 2)


print(entropy(2 / 5, 3 / 5))
