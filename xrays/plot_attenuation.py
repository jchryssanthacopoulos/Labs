"""Plot spectra for attenuation analysis."""

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
m = 0.02242843814474726
b = 0.04827938073740867


xrange = [0, 30]
yrange = [0, 70]
xticks = range(0, 40, 5)
yticks = range(0, 80, 10)


# load data
data1 = np.loadtxt("files/aluminum_0mm.txt", delimiter = "/t")
x = np.array([m * i + b for i in range(len(data1))])

data2 = np.loadtxt("files/aluminum_2mm.txt", delimiter = "/t")
data3 = np.loadtxt("files/aluminum_4mm.txt", delimiter = "/t")
data4 = np.loadtxt("files/aluminum_6mm.txt", delimiter = "/t")
data5 = np.loadtxt("files/aluminum_8mm.txt", delimiter = "/t")
data6 = np.loadtxt("files/aluminum_10mm.txt", delimiter = "/t")


# get gaussian fits
x_g1_1, y_g1_1 = fit_gauss(x, data1, 13, 15)
x_g1_2, y_g1_2 = fit_gauss(x, data1, 17.2, 18.5)
x_g2_1, y_g2_1 = fit_gauss(x, data2, 13, 15)
x_g2_2, y_g2_2 = fit_gauss(x, data2, 17.2, 18.5)
x_g3_1, y_g3_1 = fit_gauss(x, data3, 13, 15)
x_g3_2, y_g3_2 = fit_gauss(x, data3, 17.2, 18.5)
x_g4_1, y_g4_1 = fit_gauss(x, data4, 13, 15)
x_g4_2, y_g4_2 = fit_gauss(x, data4, 17.2, 18.5)
x_g5_1, y_g5_1 = fit_gauss(x, data5, 13, 15)
x_g5_2, y_g5_2 = fit_gauss(x, data5, 17.2, 18.5)
x_g6_1, y_g6_1 = fit_gauss(x, data6, 13, 15)
x_g6_2, y_g6_2 = fit_gauss(x, data6, 17.2, 18.5)


plt.rcParams.update({'font.size': 26})


# plot
plt.figure(figsize=(12, 10))
plt.plot(x, data1)
plt.plot(x_g1_1, y_g1_1, 'k', lw=3)
plt.plot(x_g1_2, y_g1_2, 'k', lw=3)
plt.grid()
plt.xlim(xrange)
plt.ylim(yrange)
plt.xticks(xticks, fontsize=35)
plt.yticks(yticks, fontsize=35)
plt.xlabel("Energy (keV)", fontsize=35)
plt.ylabel("Counts", fontsize=35)
plt.tight_layout()
plt.savefig("figures/attenuation_0cm.png")

plt.figure(figsize=(12, 10))
plt.plot(x, data2)
plt.plot(x_g2_1, y_g2_1, 'k', lw=3)
plt.plot(x_g2_2, y_g2_2, 'k', lw=3)
plt.grid()
plt.xlim(xrange)
plt.ylim(yrange)
plt.xticks(xticks, fontsize=35)
plt.yticks(yticks, fontsize=35)
plt.xlabel("Energy (keV)", fontsize=35)
plt.ylabel("Counts", fontsize=35)
plt.tight_layout()
plt.savefig("figures/attenuation_2cm.png")

plt.figure(figsize=(12, 10))
plt.plot(x, data3)
plt.plot(x_g3_1, y_g3_1, 'k', lw=3)
plt.plot(x_g3_2, y_g3_2, 'k', lw=3)
plt.grid()
plt.xlim(xrange)
plt.ylim(yrange)
plt.xticks(xticks, fontsize=35)
plt.yticks(yticks, fontsize=35)
plt.xlabel("Energy (keV)", fontsize=35)
plt.ylabel("Counts", fontsize=35)
plt.tight_layout()
plt.savefig("figures/attenuation_4cm.png")

plt.figure(figsize=(12, 10))
plt.plot(x, data4)
plt.plot(x_g4_1, y_g4_1, 'k', lw=3)
plt.plot(x_g4_2, y_g4_2, 'k', lw=3)
plt.grid()
plt.xlim(xrange)
plt.ylim(yrange)
plt.xticks(xticks, fontsize=35)
plt.yticks(yticks, fontsize=35)
plt.xlabel("Energy (keV)", fontsize=35)
plt.ylabel("Counts", fontsize=35)
plt.tight_layout()
plt.savefig("figures/attenuation_6cm.png")

plt.figure(figsize=(12, 10))
plt.plot(x, data5)
plt.plot(x_g5_1, y_g5_1, 'k', lw=3)
plt.plot(x_g5_2, y_g5_2, 'k', lw=3)
plt.grid()
plt.xlim(xrange)
plt.ylim(yrange)
plt.xticks(xticks, fontsize=35)
plt.yticks(yticks, fontsize=35)
plt.xlabel("Energy (keV)", fontsize=35)
plt.ylabel("Counts", fontsize=35)
plt.tight_layout()
plt.savefig("figures/attenuation_8cm.png")

plt.figure(figsize=(12, 10))
plt.plot(x, data6)
plt.plot(x_g6_1, y_g6_1, 'k', lw=3)
plt.plot(x_g6_2, y_g6_2, 'k', lw=3)
plt.grid()
plt.xlim(xrange)
plt.ylim(yrange)
plt.xticks(xticks, fontsize=35)
plt.yticks(yticks, fontsize=35)
plt.xlabel("Energy (keV)", fontsize=35)
plt.ylabel("Counts", fontsize=35)
plt.tight_layout()
plt.savefig("figures/attenuation_10cm.png")

plt.show()
