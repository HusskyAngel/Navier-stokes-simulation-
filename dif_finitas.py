import numpy as np


class DiferenciasFinitas():
    def __init__(self,paso:float,v0x:float,tamaño_malla:tuple):
        self.v0x=v0x
        self.paso=paso
        self.tamaño_malla=tamaño_malla

        self.beam1x=(tamaño_malla[0]//4, tamaño_malla[0]//4)  
        self.beam1y=(tamaño_malla[1],tamaño_malla[1]//4)   
        self.beam2x=(tamaño_malla[0]-(tamaño_malla[0]//4) ,tamaño_malla[0])  
        self.beam2y=(0, tamaño_malla[0]//4)  


    def __condicion(self,x,y):
        if x==0 or y==0 or x==self.tamaño_malla[0]-1 or y==self.tamaño_malla[1]-1:
            return (0,"literal")
        else:
           return (1,str(x)+","+str(y))

    def __isBeam(self,px:int,py:int)->bool:
        if (px>=self.beam1x[0] and px<= self.beam1x[0]+self.beam1x[1]) and (py >= self.tamaño_malla[1]-self.beam1y[1]):
            return True
        elif(px>=(self.tamaño_malla[0]-self.beam2x[0]))and (py <=self.beam2y[1]): 
            return True
        else:
            return False


    def terminos(self,px:int,py:int):
        #terminos={"valores":[ ],"etiqueta":[]}
        valores=[]
        etiqueta=[] 
        lista=[lambda x,y: ( 4*self.__condicion(x,y)[0], self.__condicion(x,y)[1]),
               lambda x,y: ( -1*self.__condicion(x+1,y)[0]*(2-(self.v0x*self.paso))/2, self.__condicion(x+1,y)[1]),
               lambda x,y: ( -1*self.__condicion(x-1,y)[0]*(2+(self.v0x*self.paso))/2, self.__condicion(x-1,y)[1]),
               lambda x,y: ( -1*self.__condicion(x,y+1)[0]*(2-(self.v0x*self.paso))/2, self.__condicion(x,y+1)[1]),
               lambda x,y: (-1**self.__condicion(x,y-1)[0]*(2+(self.v0x*self.paso))/2, self.__condicion(x,y-1)[1])]      

        if self.__isBeam(px,py):
            valores=np.zeros((self.tamaño_malla[0]-2)*(self.tamaño_malla[1]-2))
            valores[(px-1)+((self.tamaño_malla[0]-2)*(py-1))]=float(1)
            etiqueta=["beam" for w in range(len(valores))]
            return {"valores": valores,"etiquetas":etiqueta}
        else:
            for p in lista:
                #valor,etiqueta
                val,et=p(px,py)
                valores.append(val)
                etiqueta.append(et)
            return {"valores": valores,"etiquetas":etiqueta}
