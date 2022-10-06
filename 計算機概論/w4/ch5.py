import math
def log(x, base, epsilon):
    if x < 0 or base < 0 or epsilon < 0:
        return None
    else:
        return math.log(x, base) + epsilon

