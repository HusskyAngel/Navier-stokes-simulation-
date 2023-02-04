import numpy as np
class Utils():
    @staticmethod 
    def parsePosAFila(px:int,py:int,tamaño_malla:tuple)->int:
        return (px)+(tamaño_malla[0]*py) 

    @staticmethod
    def dDominant(X ):
        count=0
        for w in X: 
            if sum(abs(w))-abs(X[count][count])>abs(X[count][count]):
                return False
            count+=1
        return True

    @staticmethod
    def solutionTomarix(x:np.ndarray,tamaño_malla:tuple=(50,50)): 
        matrix=np.zeros((tamaño_malla[1],tamaño_malla[0]),dtype=float)
        count=0 
        for y in range(len(matrix)):
            for _x in range(len(matrix[0])):  
                matrix[y][_x]=x[count]
                count+=1
        return matrix

