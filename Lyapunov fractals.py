from PIL import Image
import numpy as np

## Parameters
string = '10'
n = 50
xmin = 2
ymin = 2
xmax = 4
ymax = 4
iter_len = 20
N = 20
#sequence S formation
for i in range(iter_len):
    string += '10'
seq = string[0:iter_len]
seq_len = len(seq)
## Image parameters
width = n
height = n
bitmap = Image.new("RGB", (width, height), "white")
pix = bitmap.load()

a = np.linspace(xmin,xmax,n)
b = np.linspace(ymin,ymax,n)
lena = int(len(a))
lenb = int(len(b))
zval = np.zeros((lena, lenb))
c = np.zeros((lena, lenb))
a0  = 0
b0   = 0
r    = 0
x    = 0
sum_log = 0
rough = 0
rough1 = 0
labda = 0

for i in range(lena):
    c[i,:] = b[i]+i*a[:]
total  =lena*lenb
prod_deriv = 0
c = np.reshape(c,-1)
zval = np.reshape(zval,-1)
for m in range(total):

    x=0.5
    b0=complex(0,c[m])
    a0=c[m]
    for rough in range(seq_len):

        if seq[rough]==1 :
          r=a0
        else:
          r=b0
        x=1*r*x*(1-x)
        sum_log = 0
        prod_deriv = 1
        rough = 1
        while ((rough <= N) and (prod_deriv < 200)):
            if seq[rough] == 1:
                r = a0
            else:
                r = b0

        x = r * x * (1 - x)
        prod_deriv = prod_deriv * r * (1 - 2 * x)
        sum_log = sum_log + np.log(0.00001 + abs(prod_deriv))
        rough = rough + 1
        labda = sum_log / N
        zval[m]=10+abs( labda )

for i in range(len(a)):
    for j in range(len(b)):
        pix[i,j] = zval[i] + zval[j]

bitmap.show()
# r = []
# x_equ = [0.5]

# for idx_x, x in enumerate(np.linspace(xmin, xmax, n)):
#     for idy_y, y in enumerate(np.linspace(ymin, ymax, n)):
#         if string[idy_y+idx_x] == 'a':
#             r.append(x)
#         else:
#             r.append(complex(0,y))
#         if idy_y > 0:
#
#             x_val = (x_equ[idy_y-1])*(r[idy_y-1])*(1-(x_equ[idy_y-1]))
#             x_equ.append(x_val)
#         else:
#             continue
#         labda = 0
#         for i in range(1, N):
#             try:
#                 labda += abs(np.log(r[idy_y-1]*(1-2*x_equ[idy_y-1])))
#             except:
#                 continue
#         labda = labda /N
#         if labda < 100:
#             labda = 1
#         else:
#             labda = 0
#         pix[idx_x, idy_y] = int(labda) * 7080
# bitmap.show()