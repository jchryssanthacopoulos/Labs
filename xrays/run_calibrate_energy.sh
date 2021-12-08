#!/bin/bash


#############
# Calibrate #
#############

# 10-min run
python find_peaks.py \
    --fn files/energy_calibration_10min.txt \
    --xgfit 600 640 --xgfit 610 630 \
    --xgfit 770 810 --xgfit 780 800 \
    --xgfit 2630 2680 --xgfit 2640 2670


# calibrate
# m = 0.022380199175391177
# b = 0.04870416329590199
python calibrate_energy.py \
    --channel 619.53,789.30,2652.84 \
    --energy 13.95,17.74,59.54

# mean - std dev
# A = 0.022464205326334332
# B = 0.17288010801630094
python calibrate_energy.py \
    --channel 613.04,782.28,2642.72 \
    --energy 13.95,17.74,59.54

# mean + std dev
# A = 0.022386390948783034
# B = -0.07504098102111101
python calibrate_energy.py \
    --channel 626.02,796.32,2662.96 \
    --energy 13.95,17.74,59.54


# get FWHM
python fwhm.py \
    --cc 0.022380199175391177,0.1768127359558065 \
    --resolution 6.49,7.02,10.12 \
    --sigma 0.35,0.24,0.75


# plot spectrum with calibrated energy
python find_peaks.py \
    --fn files/energy_calibration_10min.txt \
    --cc 0.022380199175391177,0.1768127359558065 \
    --xrange 0,60
