import numpy as np
from dif_finitas import DiferenciasFinitas
from utils import Utils

class Discretizacion():
    def __init__(self,tamaño_malla:tuple=(6,6),v0x:float=1 ) :
        self.tamaño_malla=tamaño_malla
        self.v0x=v0x
        self.paso=tamaño_malla[0]/tamaño_malla[1]

    def crearMatrizX(self):
        a=np.zeros(((self.tamaño_malla[0]-1)*(self.tamaño_malla[1]-1), ))
        b=[]
        dif=DiferenciasFinitas(paso=self.paso ,v0x= self.v0x,tamaño_malla=self.tamaño_malla)
        for row in  range(1,self.tamaño_malla[0]-1):
            for column in range(1,self.tamaño_malla[1]-1):
               
        a=np.array(a)
        b=np.array(b)
        return (a,b)
