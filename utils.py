import numpy as np
import math
class Utils():
    @staticmethod
    def dDominant(X ):
        count=0
        for w in X: 
            if sum(w)-X[count][count]>X[count][count]:
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
