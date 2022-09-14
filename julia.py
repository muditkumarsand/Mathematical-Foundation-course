from PIL import Image
import numpy as np

## Julia set Z^n + c
n = 2
cx = -0.850357820200574
cy = .017756163825227
R = 4 ## Escape radius
iter = 255
width = 600
height = 600
bitmap = Image.new("RGB", (width, height), "white")
pix = bitmap.load()


for x in range(width):
    for y in range(height):
        zx = 1.5 * (x - width / 2) / (0.5  * width)
        zy = 1.0 * (y - height / 2) / (0.5  * height)
        i = iter
        while zx * zx + zy * zy < R and i > 1:
            xtmp = (zx * zx + zy * zy) ** (n / 2) * np.cos(n * np.arctan2(zy, zx)) + cx
            zy = (zx * zx + zy * zy) ** (n / 2) * np.sin(n * np.arctan2(zy, zx)) + cy
            zx = xtmp;
            i -= 1

        ## Change here for colors
        pix[x, y] = (i << 21) + (i << 10) + i*8


bitmap.show()