import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class Utils():
    @staticmethod
    def getX(punto:str):
       aux=punto.split(',') 
       return int(aux[0])
        
    @staticmethod
    def getY(punto:str):
       aux=punto.split(',') 
       return int(aux[1])

class DiferenciasFinitas():
    def __init__(self,paso:float,v0x:float,tamaño_malla:tuple):
        self.v0x=v0x
        self.paso=paso
        self.tamaño_malla=tamaño_malla

    def __condicion(self,x,y):
        if x==0:
            return (self.v0x,"literal")
        if y==0 or y==self.tamaño_malla[1]-1 or x==self.tamaño_malla[0]-1: 
            return (0, "literal")
        else:
            return (1,str(x)+","+str(y))

    def terminos(self,px:int,py:int):
        #terminos={"valores":[ ],"etiqueta":[]}
        valores=[]
        etiqueta=[] 
        lista=[lambda x,y: ( self.__condicion(x+1,y)[0]/4, self.__condicion(x+1,y)[1]),
               lambda x,y: ( self.__condicion(x-1,y)[0]/4, self.__condicion(x-1,y)[1]),
               lambda x,y: ( -1*self.__condicion(x,y+1)[0]/4, self.__condicion(x,y+1)[1]),
               lambda x,y: ( -1*self.__condicion(x,y-1)[0]/4, self.__condicion(x,y-1)[1]),
               lambda x,y: ( -1*self.v0x*self.paso*self.__condicion(x+1,y)[0]/8, self.__condicion(x+1,y)[1]),
               lambda x,y: ( self.v0x*self.paso*self.__condicion(x-1,y)[0]/8, self.__condicion(x-1,y)[1]),
               lambda x,y: ( -1*self.__condicion(x,y)[0], self.__condicion(x,y)[1])]
        for p in lista:
            #valor,etiqueta
            val,et=p(px,py)
            valores.append(val)
            etiqueta.append(et)
        return {"valores": valores,"etiquetas":etiqueta}

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
                literal=0
                for val,et in zip(discretizacion["valores"],discretizacion["etiquetas"]):
                    if et=="literal":
                        literal+=val
                    else: 
                        aux_tam=self.tamaño_malla[0]-1
                        posx=Utils.getX(et)
                        posy=Utils.getY(et)
                        new_row[((posy-1)*aux_tam)+posx]=val
                literal*=-1
                a.append(new_row)
                b.append(literal)
                
        a=np.array(a)
        b=np.array(b)
        return (a,b)

dis=Discretizacion()
matriz=dis.crearMatrizX()
print(matriz[0])
imagen=Image.fromarray(matriz[0]*256)
imagen.show()

