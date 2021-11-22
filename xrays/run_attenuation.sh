#!/bin/bash


###############
# Attenuation #
###############

# 0 mm
# Counts @ 13.95 keV = 922-1090 => 1006 +/- 84
# Counts @ 17.74 keV = 566-630 => 598 +/- 32
python find_peaks.py \
    --fn files/aluminum_0mm.txt \
    --cc 0.02242843814474726,0.04827938073740867 \
    --title "Aluminum Attenuation (0 mm)" \
    --xgfit 13 15 --xgfit 13.5 14.5 \
    --xgfit 17.2 18.5 --xgfit 17.4 18.25

# 0.2 mm
# Counts @ 13.95 keV = 601-733 => 667 +/- 66
# Counts @ 17.74 keV = 448-483 => 466 +/- 18
python find_peaks.py \
    --fn files/aluminum_2mm.txt \
    --cc 0.02242843814474726,0.04827938073740867 \
    --title "Aluminum Attenuation (0.2 mm)" \
    --xgfit 13 15 --xgfit 13.5 14.5 \
    --xgfit 17.2 18.5 --xgfit 17.4 18.25

# 0.4 mm
# Counts @ 13.95 keV = 368-474 => 421 +/- 53
# Counts @ 17.74 keV = 329-360 => 345 +/- 16
python find_peaks.py \
    --fn files/aluminum_4mm.txt \
    --cc 0.02242843814474726,0.04827938073740867 \
    --title "Aluminum Attenuation (0.4 mm)" \
    --xgfit 13 15 --xgfit 13.5 14.5 \
    --xgfit 17.2 18.5 --xgfit 17.4 18.25

# 0.6 mm
# Counts @ 13.95 keV = 244-331 => 288 +/- 44
# Counts @ 17.74 keV = 262-284 => 273 +/- 11
python find_peaks.py \
    --fn files/aluminum_6mm.txt \
    --cc 0.02242843814474726,0.04827938073740867 \
    --title "Aluminum Attenuation (0.6 mm)" \
    --xgfit 13 15 --xgfit 13.5 14.5 \
    --xgfit 17.2 18.5 --xgfit 17.4 18.25

# 0.8 mm
# Counts @ 13.95 keV = 148-217 => 183 +/- 35
# Counts @ 17.74 keV = 187-202 => 195 +/- 8
python find_peaks.py \
    --fn files/aluminum_8mm.txt \
    --cc 0.02242843814474726,0.04827938073740867 \
    --title "Aluminum Attenuation (0.8 mm)" \
    --xgfit 13 15 --xgfit 13.5 14.5 \
    --xgfit 17.2 18.5 --xgfit 17.4 18.25

# 1.0 mm
# Counts @ 13.95 keV = 98-140 => 119 +/- 21
# Counts @ 17.74 keV = 149-161 => 155 +/- 6
python find_peaks.py \
    --fn files/aluminum_10mm.txt \
    --cc 0.02242843814474726,0.04827938073740867 \
    --title "Aluminum Attenuation (1 mm)" \
    --xgfit 13 15 --xgfit 13.5 14.5 \
    --xgfit 17.2 18.5 --xgfit 17.4 18.25


#######################
# Fit Attenuation Law #
#######################

# 13.95 keV
# mu = 20.388981077751446 cm^-1
# exp mu = 26.59 cm^-1
python fit_attenuation.py \
    --counts 1090,733,474,331,217,140 \
    --thickness 0,0.02,0.04,0.06,0.08,0.1

# low end
# mu = 22.604216313741585 cm^-1
python fit_attenuation.py \
    --counts 922,601,368,244,148,98 \
    --thickness 0,0.02,0.04,0.06,0.08,0.1

# 17.74 keV
# mu = 13.819934191498035 cm^-1
# exp mu = 13.11 cm^-1
python fit_attenuation.py \
    --counts 630,483,360,284,202,161 \
    --thickness 0,0.02,0.04,0.06,0.08,0.1

# low end
# mu = 13.602865649962979 cm^-1
python fit_attenuation.py \
    --counts 566,448,329,262,187,149 \
    --thickness 0,0.02,0.04,0.06,0.08,0.1
