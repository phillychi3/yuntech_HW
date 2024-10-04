l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
import numpy as np


def islen(l1, l2):
    if len(l1) == len(l2):
        return np.matmul(l1, l2)
    else:
        return False


print(islen(l1, l2))
