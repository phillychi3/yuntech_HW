import numpy as NP,matplotlib.pyplot as PL;
zY,n,r = 1,40,0.1;
XY = NP.tile( NP.array([[0.,0,0],[0,1,1],[1,0,1],[1,1,0]]) ,(n,1)); 
zS,zX=XY.shape; zX-=zY; 
_X,Y = XY[:,:-zY],XY[:,-zY:]; #X+= (NP.random.rand(zS,zX)-.5)r2;

for i,r in enumerate(NP.linspace(0,.7,6),231):
    X = _X + (NP.random.rand(_X.shape)-.5)r2;
    ax = PL.subplot(i);
    ax.scatter(X.T,c=NP.where(Y[:,0],'r','b'),s=1);
    ax.set_aspect('equal');

PL.show()
print(XY);
