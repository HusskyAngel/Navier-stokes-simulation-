import numpy as np
from dif_finitas import DiferenciasFinitas
from utils import Utils

class Discretizacion():
    def __init__(self,tamaño_malla:tuple=(6,6),v0x:float=1, paso: float=1/2 ) :
        self.tamaño_malla=tamaño_malla
        self.v0x=v0x
        self.paso=paso

    def crearMatrizX(self):
        a=[]
        b=[]
        dif=DiferenciasFinitas(paso=self.paso ,v0x= self.v0x,tamaño_malla=self.tamaño_malla)
        for row in  range(1,self.tamaño_malla[0]-1):
            for column in range(1,self.tamaño_malla[1]-1):
                discretizacion=dif.terminos(row,column)
                size_row=(self.tamaño_malla[0]-1)*(self.tamaño_malla[1]-1)
                new_row=np.zeros((size_row))
                literal=1 # presion constant =1/p ->1 
                for val,et in zip(discretizacion["valores"],discretizacion["etiquetas"]):
                    if et=="literal":
                        literal+=val
                    else: 
                        aux_tam=self.tamaño_malla[0]-1
                        posx=Utils.getX(et)
                        posy=Utils.getY(et)
                        px,py=Utils.transform(posx,posy,self.tamaño_malla[1]-1)
                        new_row[((py-1)*aux_tam)+px]=val
                literal*=-1
                a.append(new_row)
                b.append(literal)
                
        a=np.array(a)
        b=np.array(b)
        return (a,b)
