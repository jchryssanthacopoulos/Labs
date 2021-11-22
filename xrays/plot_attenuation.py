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


xrange = [0, 60]
yrange = [0, 70]


xgfit_peak1 = [13.5, 14.5]
xgfit_peak2 = [17.4, 18.25]


# load data
data1 = np.loadtxt("files/aluminum_0mm.txt", delimiter = "/t")
x = np.array([m * i + b for i in range(len(data1))])

data2 = np.loadtxt("files/aluminum_2mm.txt", delimiter = "/t")
data3 = np.loadtxt("files/aluminum_4mm.txt", delimiter = "/t")
data4 = np.loadtxt("files/aluminum_6mm.txt", delimiter = "/t")
data5 = np.loadtxt("files/aluminum_8mm.txt", delimiter = "/t")
data6 = np.loadtxt("files/aluminum_10mm.txt", delimiter = "/t")


# get gaussian fits
x_g1_1, y_g1_1 = fit_gauss(x, data1, float(xgfit_peak1[0]), float(xgfit_peak1[1]))
x_g1_2, y_g1_2 = fit_gauss(x, data1, float(xgfit_peak2[0]), float(xgfit_peak2[1]))


plt.rcParams.update({'font.size': 26})


# plot
plt.figure(figsize=(12, 8))
# plt.subplot(231)
plt.plot(x, data1)
# plt.plot(x_g1_1, y_g1_1)
# plt.plot(x_g1_2, y_g1_2)
plt.grid()
plt.xlim(xrange)
plt.ylim(yrange)
plt.xlabel("Energy (keV)")
plt.ylabel("Counts")
plt.savefig("figures/attenuation_0cm.png")
# plt.title("Thickness = 0 cm")

plt.figure(figsize=(12, 8))
# plt.subplot(232)
plt.plot(x, data2)
plt.grid()
plt.xlim(xrange)
plt.ylim(yrange)
plt.xlabel("Energy (keV)")
plt.ylabel("Counts")
plt.savefig("figures/attenuation_2cm.png")
# plt.title("Thickness = 0.02 cm")

plt.figure(figsize=(12, 8))
# plt.subplot(233)
plt.plot(x, data3)
plt.grid()
plt.xlim(xrange)
plt.ylim(yrange)
plt.xlabel("Energy (keV)")
plt.ylabel("Counts")
plt.savefig("figures/attenuation_4cm.png")
# plt.title("Thickness = 0.04 cm")

plt.figure(figsize=(12, 8))
# plt.subplot(234)
plt.plot(x, data4)
plt.grid()
plt.xlim(xrange)
plt.ylim(yrange)
plt.xlabel("Energy (keV)")
plt.ylabel("Counts")
plt.savefig("figures/attenuation_6cm.png")
# plt.title("Thickness = 0.06 cm")

plt.figure(figsize=(12, 8))
# plt.subplot(235)
plt.plot(x, data5)
plt.grid()
plt.xlim(xrange)
plt.ylim(yrange)
plt.xlabel("Energy (keV)")
plt.ylabel("Counts")
plt.savefig("figures/attenuation_8cm.png")
# plt.title("Thickness = 0.08 cm")

plt.figure(figsize=(12, 8))
# plt.subplot(236)
plt.plot(x, data6)
plt.grid()
plt.xlim(xrange)
plt.ylim(yrange)
plt.xlabel("Energy (keV)")
plt.ylabel("Counts")
plt.savefig("figures/attenuation_10cm.png")
# plt.title("Thickness = 0.10 cm")

plt.show()
