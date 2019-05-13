import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(xmin, xmax, ymin, ymax, granular):
    x = np.linspace(xmin, xmax, granular)
    y = np.linspace(ymin, ymax, granular)

    x, y = np.meshgrid(x, y, indexing='xy')
    c = x + 1j*y
    z = np.zeros(c.shape, dtype=c.dtype)
    iter = -np.ones(c.shape, dtype=np.int8)

    for i in range(32):
        z = z**2 + c
        iter = np.where((iter == -1) & (np.abs(z) > 2), i, iter)
        # this eventually emits overflow warnings that are safe to ignore
    
    plt.imshow(iter, extent=[xmin, xmax, ymin, ymax])
    plt.xlabel('$Re(z)$')
    plt.ylabel('$Im(z)$')
    plt.savefig('mandelbrot{}_{}_{}_{}_{}.pdf'.format(xmin, xmax, ymin, ymax, granular))
    plt.close()

mandelbrot(-2, 2, -2, 2, 1001   )
mandelbrot(0.1, 0.4, -0.1, 0.1, 1001)
