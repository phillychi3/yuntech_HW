import numpy as np

z = 6
p = 0.3
Z, O = np.zeros([z, z]), np.ones([z, z])
a = np.where(np.random.rand(z, z) < p, Z, np.random.rand(z, z))
print(
    a,
    _ := np.where(a <= 0),
    len(_[0]),
    _ := np.where(a <= 0, O, Z),
    np.sum(_),
    _ := _.sum(1),
    _.argmax(),
    sep="\n",
)
