from matplotlib import image, scale
import matplotlib.pyplot as plt
from discretization import MatrizX,MatrizY
from mapa import Map
from metodos_it import Metodos
from utils import Utils
import numpy as np
from cubic_interpolation import image_spline_interpolation

"""
Eje x 
"""
m=MatrizX()
A_x,b_x=m.matriz()
sol_x=Metodos.GaussSeidel2(25,A_x,b_x)
m=Utils.solutionTomarix(sol_x,tamaño_malla=(50,50))
#m=(m - np.min(m))/np.ptp(m)## normalization

"""
Eje y
"""
w=MatrizY()
A_y,b_y=w.matriz()
sol_y=Metodos.GaussSeidel2(25,A_y,b_y)
w=Utils.solutionTomarix(sol_y,tamaño_malla=(50,50))


"""
Plot
"""
fig,(ax1,ax2)=plt.subplots(1,2)

imx=ax1.imshow(image_spline_interpolation(m,10))
imy=ax2.imshow(image_spline_interpolation(w,10))

cbarx=fig.colorbar(imx,ax=ax1)
cbary=fig.colorbar(imy,ax=ax2)

ax1.set_title("Eje X")
ax2.set_title("Eje Y")

plt.show()


