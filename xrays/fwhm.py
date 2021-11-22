"""Find FWHM given channel resolutions."""

import argparse

import numpy as np


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get FWHM values")
    parser.add_argument("--cc", type=str, help="Calibration coefficients") 
    parser.add_argument("--resolution", type=str, help="Channel resolution") 
    parser.add_argument("--sigma", type=str, help="Channel resolution sigma") 
    args = parser.parse_args()

    m, b = [float(c) for c in args.cc.split(",")]
    resolution = [float(r) for r in args.resolution.split(",")]
    sigma = [float(s) for s in args.sigma.split(",")]

    fac = 2 * np.sqrt(2 * np.log(2))
    fwhm = [(m * r + b) * fac for r in resolution]
    fwhm_sigma = [(m * s + b) * fac for s in sigma]
    # fwhm = [m * r * fac + b for r in resolution]
    # fwhm_sigma = [m * s * fac + b for s in sigma]

    print("FWHM =", fwhm)
    print("FWHM sigma =", fwhm_sigma)
