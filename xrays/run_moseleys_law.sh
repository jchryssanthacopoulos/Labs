#!/bin/bash


# K alpha transitions
python fit_moseleys_law.py \
    --z 26,28,29,40,48 \
    --energies 6.36,7.45,8.02,15.7,23.23 \
    --sigma 0.1,0.11,0.1,0.15,0.01 \
    --xrange 600,2400 \
    --yrange 6.0,24

# lower bound (1.04e-2)
python fit_moseleys_law.py \
    --z 26,28,29 \
    --energies 6.26,7.34,7.92 \
    --sigma 0.1,0.11,0.1 \
    --xrange 600,2400 \
    --yrange 6.0,24
# upper bound (1.05e-2)
python fit_moseleys_law.py \
    --z 26,28,29 \
    --energies 6.46,7.56,8.12 \
    --sigma 0.1,0.11,0.1 \
    --xrange 600,2400 \
    --yrange 6.0,24


# K beta transitions
python fit_moseleys_law.py \
    --z 26,28,29 \
    --energies 7.03,8.22,8.87 \
    --sigma 0.1,0.13,0.11 \
    --xrange 550,850 \
    --yrange 6.50,9.50

# lower bound (1.15e-2)
python fit_moseleys_law.py \
    --z 26,28,29 \
    --energies 6.93,8.09,8.76 \
    --sigma 0.1,0.13,0.11 \
    --xrange 550,850 \
    --yrange 6.50,9.50
# upper bound (1.16e-2)
python fit_moseleys_law.py \
    --z 26,28,29 \
    --energies 7.13,8.35,8.98 \
    --sigma 0.1,0.13,0.11 \
    --xrange 550,850 \
    --yrange 6.50,9.50

# L alpha transitions
python fit_moseleys_law.py \
    --z 40,48,49 \
    --energies 2.01,3.14,3.22 \
    --sigma 0.14,0.18,0.44 \
    --xrange 1400,2400 \
    --yrange 1.8,3.75
