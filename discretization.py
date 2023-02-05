import numpy as np
from mapa import Map 
from utils import Utils
import matplotlib.pyplot as plt 


                          
class DiscretizacionX():

    def __init__(self,mapa:np.ndarray, v0:float=9., paso:float=1):
       self.mapa = mapa
       self.v0=v0
       self.paso=paso
    
    """
    E_A=2
    OUTLET_H=3
    J=4
    I=5
    INLET_F=6
    SURFACE_G=7
    D=8
    B=9
    C=10
    """

    def  retornarDiscretizacion(self,px,py):
        if self.mapa[py][px]==6:
            return {"tipo":"literal","val":self.v0 }

        elif self.mapa[py][px]==1:
            return {"tipo":"ecuacion=1","val":[
                                                  {"pos":(px,py),"n":-4},
                                                  {"pos":(px+1,py),"n":(2-(self.v0*self.paso))/2},
                                                  {"pos":(px-1,py),"n":(2+(self.v0*self.paso))/2},
                                              ]
                    }
        else:
            return {"tipo":"literal","val":0}

###crear matrix
class MatrizX():

    def __init__(self,tamaño_malla:tuple=(50,50),paso:float=1.,v0:float=1.): 
        self.tamaño_malla = tamaño_malla
        self.mapa=Map(tamaño_malla).crearMapa()

        self.paso=paso
        self.v0=v0

    def matriz(self):
        A=[]
        b=[]
        dis=DiscretizacionX(v0=self.v0,paso=self.paso,mapa=self.mapa)
        for y in range(self.tamaño_malla[1]): 
            for x in range(self.tamaño_malla[0]):
                dis_p=dis.retornarDiscretizacion(x,y)
                if dis_p["tipo"]=="literal":
                    a=np.zeros((self.tamaño_malla[0]*self.tamaño_malla[1]))
                    a[Utils.parsePosAFila(x,y,tamaño_malla=self.tamaño_malla)]=1
                    A.append(a)
                    b.append(dis_p["val"])
                elif dis_p["tipo"]=="ecuacion=1":
                    lit=0
                    a=np.zeros((self.tamaño_malla[0]*self.tamaño_malla[1]))
                    for term in dis_p["val"]:
                        aux_x,aux_y=term["pos"]
                        aux_dis=dis.retornarDiscretizacion(aux_x,aux_y)
                        if aux_dis["tipo"]!="literal":
                            a[Utils.parsePosAFila(aux_x,aux_y,self.tamaño_malla)]=term["n"]
                        else:
                            lit+=-1*term["n"]
                    A.append(a)
                    b.append(lit)
                elif dis_p["tipo"]=="ecuacion=0":
                    lit=0
                    a=np.zeros((self.tamaño_malla[0]*self.tamaño_malla[1]))
                    for term in dis_p["val"]:
                        aux_x,aux_y=term["pos"]
                        aux_dis=dis.retornarDiscretizacion(aux_x,aux_y)
                        if aux_dis["tipo"]!="literal":
                            a[Utils.parsePosAFila(aux_x,aux_y,self.tamaño_malla)]=term["n"]
                        else:
                            lit+=-1*term["n"]
                    A.append(a)
                    b.append(lit)
                
        return (np.array(A,dtype=float),np.array(b,dtype=float))
                           

class DiscretizacionY():

    def __init__(self,mapa:np.ndarray, v0:float=9., paso:float=1,mapaX:np.ndarray=np.array([])):
       self.mapa = mapa
       self.v0=v0
       self.paso=paso
       self.mapaX=mapaX
    
    """
    E_A=2
    OUTLET_H=3
    J=4
    I=5
    INLET_F=6
    SURFACE_G=7
    D=8
    B=9
    C=10
    """

    def  retornarDiscretizacion(self,px,py):
        if self.mapa[py][px]==6:
            return {"tipo":"literal","val":self.v0 }

        elif self.mapa[py][px]==1:
            
            return {"tipo":"ecuacion=1","val":[
                                                  {"pos":(px,py),"n":-4},
                                                  {"pos":(px,py+1),"n":(2-(self.v0*self.paso))/2},
                                                  {"pos":(px,py-1),"n":(2+(self.v0*self.paso))/2},
                                              ]
                    }
        #other discretizations 
#        elif self.mapa[py][px]==9:
#            return {"tipo":"literal","val":-2*(self.mapaX[py][px+1]-self.mapaX[py][px])}
        elif self.mapaX[py][px]==10:
            return {"tipo":"literal","val":-2*(self.mapaX[py+1][px]-self.mapaX[py][px])}
        elif self.mapaX[py][px]==8:
            return {"tipo":"literal","val":-2*(self.mapaX[py][px-1]-self.mapaX[py][px])}
        elif self.mapaX[py][px]==4:
            return {"tipo":"literal","val":-2*(self.mapaX[py+1][px]-self.mapaX[py][px])}
        elif self.mapaX[py][px]==5:
            return {"tipo":"literal","val":-2*(self.mapaX[py][px-1]-self.mapaX[py][px])}
        else:
            return {"tipo":"literal","val":0}

###crear matrix
class MatrizY():
 
    def __init__(self,tamaño_malla:tuple=(50,50),paso:float=1.,v0:float=1.,mapaX:np.ndarray=np.array([])): 
        self.tamaño_malla = tamaño_malla
        self.mapa=Map(tamaño_malla).crearMapa()
        self.mapaX=mapaX
        self.paso=paso
        self.v0=v0

    def matriz(self):
        A=[]
        b=[]
        dis=DiscretizacionY(v0=self.v0,paso=self.paso,mapa=self.mapa,mapaX=self.mapaX)
        for y in range(self.tamaño_malla[1]): 
            for x in range(self.tamaño_malla[0]):
                dis_p=dis.retornarDiscretizacion(x,y)
                if dis_p["tipo"]=="literal":
                    a=np.zeros((self.tamaño_malla[0]*self.tamaño_malla[1]))
                    a[Utils.parsePosAFila(x,y,tamaño_malla=self.tamaño_malla)]=1
                    A.append(a)
                    b.append(dis_p["val"])
                elif dis_p["tipo"]=="ecuacion=1":
                    lit=0
                    a=np.zeros((self.tamaño_malla[0]*self.tamaño_malla[1]))
                    for term in dis_p["val"]:
                        aux_x,aux_y=term["pos"]
                        aux_dis=dis.retornarDiscretizacion(aux_x,aux_y)
                        if aux_dis["tipo"]!="literal":
                            a[Utils.parsePosAFila(aux_x,aux_y,self.tamaño_malla)]=term["n"]
                        else:
                            lit+=-1*term["n"]
                    A.append(a)
                    b.append(lit)
                elif dis_p["tipo"]=="ecuacion=0":
                    lit=0
                    a=np.zeros((self.tamaño_malla[0]*self.tamaño_malla[1]))
                    for term in dis_p["val"]:
                        aux_x,aux_y=term["pos"]
                        aux_dis=dis.retornarDiscretizacion(aux_x,aux_y)
                        if aux_dis["tipo"]!="literal":
                            a[Utils.parsePosAFila(aux_x,aux_y,self.tamaño_malla)]=term["n"]
                        else:
                            lit+=-1*term["n"]
                    A.append(a)
                    b.append(lit)
                
        return (np.array(A,dtype=float),np.array(b,dtype=float))
                
                           



                





                





