import numpy as np

class AuxMetodos():
    @staticmethod
    def norma_infinito(x):
        return np.max(np.abs(x))

class Metodos(): 

    @staticmethod
    def GaussSeidel2(i,a,b,tol:float=0.003):
        rng = np.random.default_rng(seed=42)
        x=np.array(rng.random(b.shape),dtype=float)
        x_minus=np.zeros((len(x))) 

        for l in range(i):
            if ( (AuxMetodos.norma_infinito(x-x_minus)/AuxMetodos.norma_infinito(x)) > tol):
                x_minus=np.copy(x)
                n = len(a)
                for j in range(0, n):
                    d = b[j]
                    for i in range(0, n):
                        if(j != i):
                            d-=a[j][i] * x[i]
                    x[j] = d / a[j][j]
            else:
                print("tol cumplida en la iteracion "+str(l))
                break
        return x
