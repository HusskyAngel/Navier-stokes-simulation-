import numpy as np 

class Map():
    def __init__(self, tamaño_malla:tuple=(50,50)): 
        self.tamaño_malla = tamaño_malla

        self.beam1x=(tamaño_malla[0]//4, tamaño_malla[0]//4+tamaño_malla[0]//4)  
        self.beam1y=(tamaño_malla[1]-tamaño_malla[1]//4,tamaño_malla[1])   
        self.beam2x=(tamaño_malla[0]-(tamaño_malla[0]//4) ,tamaño_malla[0])  
        self.beam2y=(0, tamaño_malla[0]//4)  



    def crearMapa(self):
        E_A=2
        OUTLET_H=3
        J=4
        I=5
        INLET_F=6
        SURFACE_G=7
        D=8
        B=9
        C=10

        mapa=np.ones(self.tamaño_malla)
        ##BEAM1
        for y in range(self.beam1y[0],self.beam1y[1]):
            for x in range(self.beam1x[0],self.beam1x[1]):
                mapa[y][x]=0 
        ##BEAM2
        for y in range(self.beam2y[0],self.beam2y[1]):
            for x in range(self.beam2x[0],self.beam2x[1]):
                mapa[y][x]=0 

        ##D
        for w in range(self.beam1y[0],self.tamaño_malla[1]-1):
            mapa[w][self.beam1x[0]]=D
        ##C
        for w in range(self.beam1x[0],self.beam1x[1]):
            mapa[self.beam1y[0]][w]=C
        ##B
        for w in range(self.beam1y[0],self.tamaño_malla[1]-1):
            mapa[w][self.beam1x[1]]=B

        ##I
        for w in range(1,self.beam2y[1]):
            mapa[w][self.beam2x[0]]=I
        ##surface g 
        for w in range(self.tamaño_malla[0]):
            mapa[0][w]=SURFACE_G
        ##OUTLET_H
        for w in range(self.beam2y[1],self.tamaño_malla[1]):
            mapa[w][self.tamaño_malla[0]-1]=OUTLET_H
        ##E_A
        for w in range(self.tamaño_malla[0]):
            mapa[self.tamaño_malla[1]-1][w]=E_A
        ##INLET F
        for w in range(self.tamaño_malla[1]):
            mapa[w][0]=INLET_F
        ##J
        for w in range(self.beam2x[0],self.tamaño_malla[0]):
            mapa[self.beam2y[1]][w]=J


        return mapa 

