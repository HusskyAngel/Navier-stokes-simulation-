import numpy as np

class Metodos(): 
    @staticmethod
    def GaussSeidel(niter:int=25,A:np.ndarray=np.zeros((0,)),x: np.ndarray=np.zeros((0,)),b:np.ndarray=np.zeros((0,))):
        #assert( len(A)>1 and len(A[0])==len(b) and len(A[0])==len(x))
        for i in range(0,niter):
            #Finding length of a(3)       
            n = len(A)                   
            # for loop for 3 times as to calculate x, y , z
            for j in range(0, n):        
                # temp variable d to store b[j]
                d = b[j]                  
                # to calculate respective xi, yi, zi
                for i in range(0, n):     
                    if(j != i):
                        d-=A[j][i] * x[i]
                # updating the value of our solution        
                x[j] = d / A[j][j]
        return x
