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
m = 0.022380199175391177
b = 0.1768127359558065


xrange = [0, 70]
yrange = [0, 110]


# load data
data1 = np.loadtxt("files/energy_calibration_10min.txt", delimiter = "/t")
x = np.array([m * i + b for i in range(len(data1))])

# get gaussian fits
xg_1, yg_1 = fit_gauss(x, data1, 13.6, 14.5)
xg_2, yg_2 = fit_gauss(x, data1, 17.4, 18.3)
xg_3, yg_3 = fit_gauss(x, data1, 59.04, 60.16)

# plot
plt.figure(figsize=(8, 6))
plt.plot(x, data1, lw=1)
plt.plot(xg_1, yg_1, 'k', lw=2)
plt.plot(xg_2, yg_2, 'k', lw=2)
plt.plot(xg_3, yg_3, 'k', lw=2)
plt.grid()
plt.xlim(xrange)
plt.ylim(yrange)
plt.xticks(range(0, 80, 10), fontsize=17)
plt.yticks(range(0, 120, 10), fontsize=17)
plt.xlabel("Energy (keV)", fontsize=17)
plt.ylabel("Counts", fontsize=17)
plt.show()
