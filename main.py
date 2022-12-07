import numpy as np
from PIL import Image
from discretization import Discretizacion
import numpy as np
from utils import Utils

dis=Discretizacion()
A,b=dis.crearMatrizX()
print(Utils.dDominant(A))
print(A)
imagen=Image.fromarray(A*562)
imagen.show()

