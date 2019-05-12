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
    orders = (0, 0.5, 1, 2, 12)
    mybessels = [bessel(xs, order) for order in orders]
    realbessels = [special.jv(order, xs) for order in orders]
    for m, ys_bessel in zip(orders, mybessels):
        plt.plot(xs, ys_bessel, 'My bessel function of order', m)
    for m, ys_bessel in zip(orders, realbessels):
        plt.plot(xs, ys_bessel, 'Real bessel function of order', m)
    plt.save(name)

do_plot('bessels.pdf')
