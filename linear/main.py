import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from discretization import Discretizacion
import numpy as np
from utils import Utils
from metodos_it import Metodos


if __name__=="__main__":
    tamaño_malla=(50,50)
    dis=Discretizacion(tamaño_malla=tamaño_malla)
    A,b=dis.crearMatrizX()
    print(A)
    solucion=Metodos.GaussSeidel2(100,A,b)
    print(Utils.solutionTomarix(solucion,tamaño_malla=tamaño_malla))
    plt.imshow(Utils.solutionTomarix(solucion,tamaño_malla=tamaño_malla)) 
    plt.colorbar()
    plt.show()



