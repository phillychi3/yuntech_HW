import numpy as NP
from functools import reduce

NP.set_printoptions(linewidth=30)

def mul1(a):
    s = 1
    for i in a:
        s *= i
    return s

mul2 = lambda a: reduce(lambda x, y: x*y, a)

sp = (2, 3, 4)
a = NP.arange(mul1(sp))
b = a.reshape(sp)
print(a.shape, sep='\n')
print(b, b.shape)

sp = (2, 3, 2, 4)
a = NP.arange(mul2(sp))
b = a.reshape(sp)
print(a.shape, a)
print(b, b.shape)