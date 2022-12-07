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
    solucion=Metodos.GaussSeidel(A=A,b=b,x=np.zeros(b.shape))  
    plt.imshow(Utils.solutionTomarix(solucion,tamaño_malla=tamaño_malla), cmap='hot')
    plt.colorbar()
    plt.show()
    #imagen=Image.fromarray(A*562)
    #imagen.show()



