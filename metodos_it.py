import numpy as np

class Metodos(): 

    @staticmethod
    def GaussSeidel2(i,a,b):
        x=np.array(np.zeros(b.shape),dtype=float)
        for l in range(i):
            n = len(a)
            for j in range(0, n):
                d = b[j]
                for i in range(0, n):
                    if(j != i):
                        d-=a[j][i] * x[i]
                x[j] = d / a[j][j]
        return x
