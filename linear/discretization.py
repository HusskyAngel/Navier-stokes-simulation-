import numpy as np
from dif_finitas import DiferenciasFinitas
from utils import Utils

class Discretizacion():
    def __init__(self,tamaño_malla:tuple=(25,25),v0x:float=1,paso:float=1 ) :
        self.tamaño_malla=tamaño_malla
        self.v0x=v0x
        self.paso=paso

    def crearMatrizX(self):
        a=[]
        b=[]
        dif=DiferenciasFinitas(paso=self.paso ,v0x= self.v0x,tamaño_malla=self.tamaño_malla)
        for column in  range(1,self.tamaño_malla[1]-1):
            for row in range(1,self.tamaño_malla[0]-1):
                p=np.zeros((self.tamaño_malla[0]-2) * (self.tamaño_malla[1]-2))
                lit=1
                dd=dif.terminos(row,column)
                for val,et in zip(dd["valores"],dd["etiquetas"]):
                    if et=="literal":
                        lit+=float(val)
                    elif et=="beam":
                        p=dd["valores"]
                        lit=1
                        break
                    else:
                        px=Utils.getX(et)
                        py=Utils.getY(et)
                        p[(px-1)+((self.tamaño_malla[0]-2)*(py-1))]=float(val)
                b.append(lit)
                a.append(p)
               
        a=np.array(a,dtype=float)

        b=np.array(b,dtype=float)
        return (a,b)
