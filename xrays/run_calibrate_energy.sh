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
python calibrate_energy.py \
    --channel 619.53,780.30,2652.84 \
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


# calibrate with different mean +/- std dev
# 612.49 - 626.18
# 782.089 - 796.599
# 2641.602 - 2663.334

# mean
# A = 0.02242843814474726
# B = 0.04827938073740867
python calibrate_energy.py \
    --channel 619.334,789.344,2652.468 \
    --energy 13.95,17.74,59.54

# mean - std dev
# A = 0.02247252198379239
# B = 0.1756112489782815
python calibrate_energy.py \
    --channel 612.49,782.089,2641.602 \
    --energy 13.95,17.74,59.54

# mean + std dev
# A = 0.022384539775794927
# B = -0.07858632563091561
python calibrate_energy.py \
    --channel 626.18,796.599,2663.334 \
    --energy 13.95,17.74,59.54
