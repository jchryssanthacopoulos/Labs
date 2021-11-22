"""Find peaks in a spectrum."""

import argparse
from typing import List, Optional

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sci_signal
import scipy.optimize as opt


def find_peaks(
        x: np.array,
        data: np.array,
        data_bg: Optional[np.array] = None,
        xmin: Optional[float] = None,
        xmax: Optional[float] = None,
        height: Optional[int] = None,
        threshold: Optional[int] = None,
        xgfit: Optional[List] = None,
        title: Optional[str] = None,
        subtractbg: Optional[bool] = False
):
    # find peaks
    peaks, _ = sci_signal.find_peaks(data, height=height, threshold=threshold)
    print("Peaks at", [x[p] for p in peaks])

    # plot
    if data_bg is not None:
        if subtractbg:
            # subtract background and floor to zero
            # do not plot
            data -= data_bg
            data = np.array([max(0, d) for d in data])
        else:
            plt.plot(x, data_bg, label="background")
    plt.plot(x, data, label="sample", lw=0.5)

    # fit gaussians
    if xgfit:
        for idx, xrange in enumerate(xgfit):
            x_g, y_g, mu, sigma, int_raw, int_fit = fit_gauss(
                x, data, float(xrange[0]), float(xrange[1])
            )
            label = "Fit {}: mu {:.3f}, sigma: {:.3f}, integral: {} (raw) / {} (fit)".format(
                idx + 1, mu, sigma, int(int_raw), int(int_fit)
            )
            print(label)
            plt.plot(x_g, y_g)

    plt.grid()
    plt.xlabel("Energy (keV)")
    plt.ylabel("Counts")

    if title:
        plt.title(title)

    plt.xlim([xmin, xmax])
    plt.show()


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

    return x, y_fit, coeff[1], coeff[2], sum(y), sum(y_fit)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find peaks in provided spectrum")
    parser.add_argument("--fn", type=str, help="File to find peaks for") 
    parser.add_argument("--bg", type=str, help="File of background") 
    parser.add_argument("--cc", type=str, help="Calibration coefficients") 
    parser.add_argument("--title", type=str, help="Title of plot") 
    parser.add_argument("--xrange", type=str, help="X range in plot") 
    parser.add_argument("--height", type=int, help="Height to search for peaks") 
    parser.add_argument("--threshold", type=int, help="Threshold to search for peaks") 
    parser.add_argument("--xgfit", action='append', nargs=2, metavar=('xmin', 'xmax'), help='X range for Gaussian fit')
    parser.add_argument('--subtractbg', action='store_true')
    args = parser.parse_args()

    # parase arguments
    filename = args.fn
    calib_coeff = args.cc
    filename_bg = args.bg
    xrange = args.xrange
    height = args.height
    threshold = args.threshold
    xgfit = args.xgfit
    title = args.title
    subtractbg = args.subtractbg

    data = np.loadtxt(filename, delimiter = "/t")

    if calib_coeff:
        m, b = [float(c) for c in calib_coeff.split(",")]
        x = np.array([m * i + b for i in range(len(data))])
    else:
        x = np.array(range(len(data)))

    data_bg = None
    if filename_bg:
        data_bg = np.loadtxt(filename_bg, delimiter = "/t")

    x_min = None
    x_max = None
    if xrange:
        x_min, x_max = [float(c) for c in xrange.split(",")]

    find_peaks(x, data, data_bg, x_min, x_max, height, threshold, xgfit, title, subtractbg)
