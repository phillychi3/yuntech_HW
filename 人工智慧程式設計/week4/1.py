import numpy as np

v, h = np.array([1.0, 4, 9]), np.array([1.0, 3, 5, 7])
n, m = v.sum() * h.sum() * 3, v.reshape(3, 1) * h.reshape(1, 4)
v /= v.sum() / n
h /= h.sum() / n
m /= m.sum() / n
M = np.zeros([m.shape[0] + 1, m.shape[1] + 1])
M[:-1, -1] = v
M[-1, :-1] = h
M[:-1, :-1] = m
M[-1, -1] = n
print(
    v.shape,
    v,
    v.sum(),
    h.shape,
    h,
    h.sum(),
    m.shape,
    m,
    m.sum(),
    M.shape,
    M,
    M.sum(),
    sep="\n",
)
