from PIL import Image
import numpy as np

## Defining the function and its derivative
func = 'np.cosh(z) - 1'
func_der = 'np.sinh(z)'

## Defining the parameters
tol = 1e-6
xmin = -2
ymin = -2
xmax = 2
ymax = 2 ## Defines the bound under complex plane
n= 900 ## grid in this bound
iter = 500


## Function for getting the root
def root_newt(f,f_der,z_init,maxiter = iter):
    z = z_init
    k = 0
    while k < maxiter:
        f_val = eval(f)
        fder_val = eval(f_der)
        step = f_val/fder_val
        if abs(step) <= tol:
            return z, k
        z -= step
        k += 1
    return None,None
## To get the index of the root
def get_root_index(root, r, tol = tol):

    try:

        return np.asarray(np.isclose(root, r, atol=tol)).nonzero()[0][0]
    except:
        root.append(r)

        return len(root) - 1

def plot_fractal(f,f_der,n=n,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax):

    root = []

    ## Image parameters
    width = n
    height = n
    bitmap = Image.new("RGB", (width, height), "white")
    pix = bitmap.load()
    for idx_x, x in enumerate(np.linspace(xmin, xmax, n)):
        for idy_y, y in enumerate(np.linspace(ymin, ymax, n)):
            z_init = complex(x,y)
            r,iter_val = root_newt(f,f_der,z_init)

            if r is not None:
                idx_r = get_root_index(root, r)
                #print(type(idx_r))


    ### drawing image
                ## Changing the multiplication value will change the color pattern of image

                pix[idx_x ,idy_y] = int(idx_r) * 7080  + iter_val * 680
    bitmap.show()

plot_fractal(func,func_der)



