import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4,4)
ex,eX=np.exp(x),np.exp(-x)

for i,y in enumerate([
    1/(1+ex),
    (ex-eX)/(ex+eX),
    np.maximum(x,0),
    np.where(x>0,x,0.1*x),
    np.where(x>0,x,np.exp(x)-1)
],231):
    plt.subplot(i).plot(x,y)

plt.show()