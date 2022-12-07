import numpy as np
from PIL import Image
from discretization import Discretizacion
import numpy as np
from utils import Utils

dis=Discretizacion()
A,b=dis.crearMatrizX()
print(Utils.dDominant((A+(-1*Utils.minimun(A))+1) *256))
print(A)
imagen=Image.fromarray(A*562)
imagen.show()

