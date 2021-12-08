"""Plot spectra for mono-elemental samples."""

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


# load data
data_fe = np.loadtxt("files/spectrum_fe.txt", delimiter = "/t")
x = np.array([m * i + b for i in range(len(data_fe))])

data_ni = np.loadtxt("files/spectrum_ni.txt", delimiter = "/t")
data_cu = np.loadtxt("files/spectrum_cu.txt", delimiter = "/t")
data_sn = np.loadtxt("files/spectrum_sn.txt", delimiter = "/t")
data_cd = np.loadtxt("files/spectrum_cd.txt", delimiter = "/t")
data_in = np.loadtxt("files/spectrum_in.txt", delimiter = "/t")
data_zr = np.loadtxt("files/spectrum_zr.txt", delimiter = "/t")

# remove background
data_bg = np.loadtxt("files/generator_background.txt", delimiter = "/t")
data_fe = np.array([max(0, d) for d in data_fe - data_bg])
data_ni = np.array([max(0, d) for d in data_ni - data_bg])
data_cu = np.array([max(0, d) for d in data_cu - data_bg])
data_sn = np.array([max(0, d) for d in data_sn - data_bg])
data_cd = np.array([max(0, d) for d in data_cd - data_bg])
data_in = np.array([max(0, d) for d in data_in - data_bg])
data_zr = np.array([max(0, d) for d in data_zr - data_bg])

# get gaussian fits
xg_fe_1, yg_fe_1 = fit_gauss(x, data_fe, 6, 6.7)
xg_fe_2, yg_fe_2 = fit_gauss(x, data_fe, 6.7, 7.4)

xg_ni_1, yg_ni_1 = fit_gauss(x, data_ni, 7, 8)
xg_ni_2, yg_ni_2 = fit_gauss(x, data_ni, 7.8, 8.6)

xg_cu_1, yg_cu_1 = fit_gauss(x, data_cu, 7.6, 8.4)
xg_cu_2, yg_cu_2 = fit_gauss(x, data_cu, 8.5, 9.2)

xg_sn_1, yg_sn_1 = fit_gauss(x, data_sn, 3.4, 3.8)

xg_cd_1, yg_cd_1 = fit_gauss(x, data_cd, 23, 23.5)
xg_cd_2, yg_cd_2 = fit_gauss(x, data_cd, 2.6, 3.6)

xg_in_1, yg_in_1 = fit_gauss(x, data_in, 2.8, 4)

xg_zr_1, yg_zr_1 = fit_gauss(x, data_zr, 15.4, 16)
xg_zr_2, yg_zr_2 = fit_gauss(x, data_zr, 1.7, 2.2)


plt.rcParams.update({'font.size': 26})


# plot
plt.figure(figsize=(12, 10))
plt.plot(x, data_fe, lw=2)
plt.plot(xg_fe_1, yg_fe_1, label="K-alpha", lw=2)
plt.plot(xg_fe_2, yg_fe_2, label="K-beta", lw=2)
plt.grid()
plt.legend()
plt.xlim([0, 16])
plt.xticks(range(0, 18, 2), fontsize=35)
plt.yticks(fontsize=35)
plt.xlabel("Energy (keV)", fontsize=35)
plt.ylabel("Counts", fontsize=35)
plt.tight_layout()
plt.savefig("figures/fe_spectrum.png")

plt.figure(figsize=(12, 10))
plt.plot(x, data_ni, lw=2)
plt.plot(xg_ni_1, yg_ni_1, label="K-alpha", lw=2)
plt.plot(xg_ni_2, yg_ni_2, label="K-beta", lw=2)
plt.grid()
plt.legend()
plt.xlim([0, 16])
plt.xticks(range(0, 18, 2), fontsize=35)
plt.yticks(fontsize=35)
plt.xlabel("Energy (keV)", fontsize=35)
plt.ylabel("Counts", fontsize=35)
plt.tight_layout()
plt.savefig("figures/ni_spectrum.png")

plt.figure(figsize=(12, 10))
plt.plot(x, data_cu, lw=2)
plt.plot(xg_cu_1, yg_cu_1, label="K-alpha", lw=2)
plt.plot(xg_cu_2, yg_cu_2, label="K-beta", lw=2)
plt.grid()
plt.legend()
plt.xlim([0, 16])
plt.xticks(range(0, 18, 2), fontsize=35)
plt.yticks(fontsize=35)
plt.xlabel("Energy (keV)", fontsize=35)
plt.ylabel("Counts", fontsize=35)
plt.tight_layout()
plt.savefig("figures/cu_spectrum.png")

plt.figure(figsize=(12, 10))
plt.plot(x, data_sn, lw=2)
plt.plot(xg_sn_1, yg_sn_1, label="L-beta", lw=2)
plt.grid()
plt.legend()
plt.xlim([0, 16])
plt.xticks(range(0, 18, 2), fontsize=35)
plt.yticks(fontsize=35)
plt.xlabel("Energy (keV)", fontsize=35)
plt.ylabel("Counts", fontsize=35)
plt.tight_layout()
# plt.gca().tick_params(axis='y', which='major', pad=30)
plt.savefig("figures/sn_spectrum.png")

plt.figure(figsize=(12, 10))
plt.plot(x, data_cd, lw=2)
plt.plot(xg_cd_1, yg_cd_1, label="K-alpha", lw=2)
plt.plot(xg_cd_2, yg_cd_2, label="L-alpha", lw=2)
plt.grid()
plt.legend()
plt.xlim([0, 25])
plt.xticks(fontsize=35)
plt.yticks(fontsize=35)
plt.xlabel("Energy (keV)", fontsize=35)
plt.ylabel("Counts", fontsize=35)
plt.tight_layout()
plt.savefig("figures/cd_spectrum.png")

plt.figure(figsize=(12, 10))
plt.plot(x, data_in, lw=2)
plt.plot(xg_in_1, yg_in_1, label="L-alpha", lw=2)
plt.grid()
plt.legend()
plt.xlim([0, 16])
plt.xticks(range(0, 18, 2), fontsize=35)
plt.yticks(fontsize=35)
plt.xlabel("Energy (keV)", fontsize=35)
plt.ylabel("Counts", fontsize=35)
plt.tight_layout()
plt.savefig("figures/in_spectrum.png")

plt.figure(figsize=(12, 10), linewidth=5)
plt.plot(x, data_zr, lw=2)
plt.plot(xg_zr_1, yg_zr_1, label="K-alpha", lw=2)
plt.plot(xg_zr_2, yg_zr_2, label="L-alpha", lw=2)
plt.grid()
plt.legend()
plt.xlim([0, 20])
plt.xticks(range(0, 25, 5), fontsize=35)
plt.yticks(fontsize=35)
plt.xlabel("Energy (keV)", fontsize=35)
plt.ylabel("Counts", fontsize=35)
plt.tight_layout()
plt.savefig("figures/zr_spectrum.png")

plt.tight_layout()
plt.show()
