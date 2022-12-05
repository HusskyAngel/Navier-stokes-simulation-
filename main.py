import numpy as np
from PIL import Image
from discretization import Discretizacion
import numpy as np


dis=Discretizacion()
A,b=dis.crearMatrizX()
imagen=Image.fromarray(A*562)
imagen.show()

