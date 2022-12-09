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
    def solutionTomarix(x:np.ndarray,tamaño_malla:tuple=(25,25)): 
        matrix=np.zeros((tamaño_malla[0]-2,tamaño_malla[1]-2),dtype=float)
        count=0
        count_y=0
        print("________________________")
        print(x.shape," xshape")
        print("________________________")
        while count<x.shape[0]-1:
            for t in range(tamaño_malla[0]-2):
                if type(x[t+count])!=float: 
                    matrix[count_y][t]=0
                else:
                    matrix[count_y][t]=x[t+count]
            count+=tamaño_malla[0]-2
            count_y+=1
        return matrix


