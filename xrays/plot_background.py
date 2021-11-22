"""Plot generator background."""

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt


def fit_gauss(x: np.array, y: np.array, x_min: float, x_max: float):
    """Fit Gaussian to range of data.

    Args:
        x: Independent variable
        y: Dependent variable
        x_min: Minimum of x to fit Gaussian
        x_max: Maximum of x to fit Gaussian

    Returns:
        Tuple of selected x range and fitted Gaussian, and mean and std dev

    """
    # gaussian function
    def gauss(x, A, mu, sigma):
        return A * np.exp(-(x - mu)**2 / (2. * sigma**2))

    # select data
    data_in_range = np.logical_and(x >= x_min, x <= x_max)
    x = x[data_in_range]
    y = y[data_in_range]

    # fit gaussian
    p0 = (y.max(), x.mean(), x.max() - x.min())
    coeff, _ = opt.curve_fit(gauss, x, y, p0=p0, maxfev=100000)

    y_fit = gauss(x, *coeff)

    return x, y_fit


# calibration coefficients
m = 0.0224131
b = 0.03844653


xrange = [0, 15]
yrange = [0, 20]


# load data
data1 = np.loadtxt("files/generator_background.txt", delimiter = "/t")
x = np.array([m * i + b for i in range(len(data1))])

# get gaussian fits
xg_1, yg_1 = fit_gauss(x, data1, 2.35, 2.85)
xg_2, yg_2 = fit_gauss(x, data1, 2.6, 3.3)
xg_3, yg_3 = fit_gauss(x, data1, 7.3, 8.6)
xg_4, yg_4 = fit_gauss(x, data1, 8.5, 10)
xg_5, yg_5 = fit_gauss(x, data1, 10, 11)
xg_6, yg_6 = fit_gauss(x, data1, 12, 13.2)

# plot
plt.figure(figsize=(8, 6))
plt.plot(x, data1, lw=1)
plt.plot(xg_1, yg_1, 'k')
plt.plot(xg_2, yg_2, 'k')
plt.plot(xg_3, yg_3, 'k')
plt.plot(xg_4, yg_4, 'k')
plt.plot(xg_5, yg_5, 'k')
plt.plot(xg_6, yg_6, 'k')
plt.grid()
plt.xlim(xrange)
plt.ylim(yrange)
plt.xlabel("Energy (keV)")
plt.ylabel("Counts")
plt.show()
