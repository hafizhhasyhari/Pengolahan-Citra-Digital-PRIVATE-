import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for i in range(max_iter):
        if abs(z) > 2:
            return i
        z = z*z + c
    return max_iter

width, height = 800, 800
xmin, xmax = -2, 2
ymin, ymax = -2, 2

image = np.zeros((width, height))

for x in range(width):
    for y in range(height):
        cx = xmin + (x / width) * (xmax - xmin)
        cy = ymin + (y / height) * (ymax - ymin)
        image[x, y] = mandelbrot(complex(cx, cy), 100)

plt.imshow(image.T, cmap="inferno", extent=[xmin, xmax, ymin, ymax])
plt.colorbar()
plt.title("Mandelbrot Fractal")
plt.show()
