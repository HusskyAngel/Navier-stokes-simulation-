import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from discretization import Discretizacion
import numpy as np
from utils import Utils
from metodos_it import Metodos


if __name__=="__main__":
    tamaño_malla=(25,25)
    dis=Discretizacion(tamaño_malla=tamaño_malla)
    A,b=dis.crearMatrizX()
    print(Utils.dDominant(A))
    print(A.shape)
#    solucion=Metodos.GaussSeidel(A=A,b=b,x=np.zeros(b.shape))  
    solucion=Metodos.GaussSeidel2(25,A,b,np.zeros((23*23)))
    print(solucion)
    f=Utils.solutionTomarix(solucion,tamaño_malla=tamaño_malla)
    plt.imshow(Utils.solutionTomarix(f,tamaño_malla=tamaño_malla)) 
    plt.show()
    #imagen=Image.fromarray(A*562)
    #imagen.show()



