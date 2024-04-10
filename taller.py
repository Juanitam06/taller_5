#importar la biblioteca numpy y crearle un alias
import numpy as np  
#importar/llamar la biblioteca matplotlib y crearle un alias
import matplotlib.pyplot as plt  
#define una funcion con sus respectivos paramentros, en este caso maxit y r tienen un valor inicial
def mandelbrot(h, w, maxit=20, r=2):  
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    #para hallar el valor de x se usa la funcion linspace el cual recible un rango de numeros entre -2.5 y 1.5
    #y el argumento de esto es cuatro por "h" mas uno
    x = np.linspace(-2.5, 1.5, 4*h+1) 
    #para hallar el valor de y se usa la funcion linspace el cual recible un rango de numeros entre -1.5 y 1.5
    #y el argumento de esto es tres por "w" mas uno
    y = np.linspace(-1.5, 1.5, 3*w+1)
    #con la funcion meshgrid hacemos una asignacion multiple en A y B
    A, B = np.meshgrid(x, y)
    #El valor de C se determina en la suma de A mas B por1
    C = A + B*1j
    z = np.zeros_like(C)
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + C
        diverge = abs(z) > r                    # who is diverging
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i                    # note when
        z[diverge] = r                          # avoid diverging too much

    return divtime
plt.clf()
plt.imshow(mandelbrot(400, 400))
