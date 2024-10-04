import math


def log(x, base, epsilon):
    if x < 0 or base < 0 or epsilon < 0:
        return None
    else:
        return math.log(x, base) + epsilon


def logg(x, base, epsilon):
    lower_bound = 0
    while base**lower_bound < x:
        lower_bound += 1
    low = lower_bound - 1
    high = lower_bound + 1
    # perform bisection search
    ans = (high + low) / base
    while abs(base**ans - x) >= epsilon:
        if base**ans < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / base
    print(ans, "is close to the log base 2 of", x)
