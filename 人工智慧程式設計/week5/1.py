import numpy as np

array = np.arange(7)


print(np.lib.stride_tricks.as_strided(array, shape=(4, 4), strides=(4, 4)))
