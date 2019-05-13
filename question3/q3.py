import numpy as np
import scipy.integrate as integrate
import scipy.special as special
import matplotlib.pyplot as plt

def bsl_integrand(t, x, m):
    return np.cos(m * t - x * np.sin(t))

def bessel(x, m):
    # integrate and discard error bound
    return (integrate.quad(bsl_integrand, 0, np.pi, args=(x, m)))[0] / np.pi

bessel = np.vectorize(bessel)

def do_plot(name):
    xs = np.linspace(0., 4 * np.pi, 150)
    orders = (0, 1, 2, 12)
    mybessels = [bessel(xs, order) for order in orders]
    realbessels = [special.jv(order, xs) for order in orders]
    for m, ys_bessel in zip(orders, mybessels):
        plt.plot(xs, ys_bessel, label='My bessel function of order {}'.format(m))
    for m, ys_bessel in zip(orders, realbessels):
        plt.plot(xs, ys_bessel, linestyle=':', label='Actual bessel function of order {}'.format(m))
    plt.legend()    
    plt.xlabel('$x$')
    plt.ylabel('$J_m(x)$')
    plt.savefig(name)

do_plot('bessels.pdf')

print('Part b')

def airy(x):
    base_intensity = 1.
    return 4 * base_intensity * (special.jv(1, x) / x)**2

# x = qpi / lambda f
print('For light and telescopt with wavelength 1 m, f-number 1, aperture radius 1 m')
granular = 100
wavelength = 1
aperture = 1
f_num = 1
plt.close()

plt.figure()

x = np.linspace(-aperture, aperture, granular)
y = np.linspace(-aperture, aperture, granular)
X, Y = np.meshgrid(x, y)
dists = np.array([[np.sqrt(xx**2 + yy**2) for yy in y] for xx in y]).reshape(granular, granular)
airy_out = airy(dists * np.pi / wavelength / f_num)
plt.pcolormesh(X, Y, airy_out, cmap='binary')
plt.xlabel("x (m)")
plt.ylabel("y (m)")

plt.savefig('airy.pdf')
