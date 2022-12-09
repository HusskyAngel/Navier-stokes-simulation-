import numpy as np
import math
import sys

class Utils():
    @staticmethod
    def dDominant(X ):
        count=0
        for w in X: 
            if sum(abs(w))-abs(X[count][count])>abs(X[count][count]):
                return False
            count+=1
        return True
    @staticmethod
    def getX(punto:str):
        aux=punto.split(',') 
        return int(aux[0])
        
    @staticmethod
    def getY(punto:str):
       aux=punto.split(',') 
       return int(aux[1])

    @staticmethod
    def transform(x:int,y:int,y_max:int):
       return (x,y_max-y)


    @staticmethod 
    def minimun(m):
        mini=math.inf
        for  x in m:
            for y in x:
                if y<mini:
                    mini=y
        return mini
    @staticmethod 
    def solutionTomarix(x:np.ndarray=np.zeros((0,)),tamaño_malla:tuple=(25,25)): 
        matrix=np.zeros((tamaño_malla[0]-1,tamaño_malla[1]-1),dtype=float)
        count=0
        count_y=0
        while count<x.shape[0]-1:
            for t in range(tamaño_malla[0]-1):
                matrix[count_y][t]=x[t+count]
            count+=tamaño_malla[0]-1
            count_y+=1
        return matrix


