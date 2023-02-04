import numpy as np
import scipy.interpolate as spi

def image_spline_interpolation(image, scale_factor):
    rows, cols = image.shape
    x = np.linspace(0, cols-1, cols)
    y = np.linspace(0, rows-1, rows)
    x_interp = np.linspace(0, cols-1, int(cols*scale_factor))
    y_interp = np.linspace(0, rows-1, int(rows*scale_factor))
    interp_func = spi.RectBivariateSpline(y, x, image)
    return interp_func(y_interp, x_interp)

