import numpy as np

class Metodos(): 
    @staticmethod
    def GaussSeidel(niter:int=25,A:np.array=np.zeros((25,25)),x:list):
