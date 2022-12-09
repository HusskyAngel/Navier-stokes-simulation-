import numpy as np

class Metodos(): 
    @staticmethod
    def GaussSeidel(niter:int=25,A:np.ndarray=np.zeros((0,)),x: np.ndarray=np.zeros((0,)),b:np.ndarray=np.zeros((0,))):
        L=np.tril(A)
        U=A-L
        for i in range(niter):
            x=np.dot(np.linalg.inv(L),b-np.dot(U,x))
        return x

    @staticmethod
    def GaussSeidel2(i,a,b):
        #Finding length of a(3)       
        print(b.shape)
        x=np.array(np.zeros(b.shape),dtype=float)
        for l in range(i):
            n = len(a)
            # for loop for 3 times as to calculate x, y , z
            for j in range(0, n):
                d = b[j]
                for i in range(0, n):
                    if(j != i):
                        d-=a[j][i] * x[i]
                x[j] = d / a[j][j]
        return x
