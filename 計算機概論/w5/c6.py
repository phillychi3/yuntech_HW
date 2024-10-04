tt = {"1": 1, "2": 2, "3": 3}


def isin(s):
    if s in tt:
        return tt[s]
    else:
        return -1


print(isin("1"))
print(isin("4"))
