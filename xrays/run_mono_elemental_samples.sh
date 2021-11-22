#!/bin/bash


# iron
python find_peaks.py \
    --fn files/spectrum_fe.txt \
    --bg files/generator_background.txt \
    --cc 0.02241310493166304,0.038446520796036054 \
    --title "Iron Spectrum" \
    --xrange 2,16 \
    --subtractbg \
    --xgfit 6 6.7 --xgfit 6.1 6.6 \
    --xgfit 6.7 7.4 --xgfit 6.85 7.25


# nickel
python find_peaks.py \
    --fn files/spectrum_ni.txt \
    --bg files/generator_background.txt \
    --cc 0.02241310493166304,0.038446520796036054 \
    --title "Nickel Spectrum" \
    --xrange 2,16 \
    --subtractbg \
    --xgfit 7 8 --xgfit 7.1 7.8 \
    --xgfit 7.8 8.6 --xgfit 8 8.44


# copper
python find_peaks.py \
    --fn files/spectrum_cu.txt \
    --bg files/generator_background.txt \
    --cc 0.02241310493166304,0.038446520796036054 \
    --title "Copper Spectrum" \
    --xrange 2,16 \
    --subtractbg \
    --xgfit 7.6 8.4 --xgfit 7.8 8.3 \
    --xgfit 8.5 9.2 --xgfit 8.6 9.1


# tin
# K alpha: 25.2713 25.0440 (not found)
# K beta: 28.4860 (not found)
# L alpha: 3.44398 3.43542
# L beta: 3.66280 3.90486 (detected)
# L gamma: 4.13112
python find_peaks.py \
    --fn files/spectrum_sn.txt \
    --bg files/generator_background.txt \
    --cc 0.02241310493166304,0.038446520796036054 \
    --title "Tin Spectrum" \
    --xrange 0,20 \
    --subtractbg \
    --xgfit 3.4 3.8 --xgfit 3.55 3.7


# cadmium
# K alpha: 23.1736 22.9841 (detected)
# K beta: 26.0955 (spike, but it's really low)
# L alpha: 3.13373 3.12691 (detected)
# L beta: 3.31657 3.52812
# L gamma: 3.71686 (detected)
python find_peaks.py \
    --fn files/spectrum_cd.txt \
    --bg files/generator_background.txt \
    --cc 0.02241310493166304,0.038446520796036054 \
    --title "Cadmium Spectrum" \
    --xrange 0,30 \
    --subtractbg \
    --xgfit 23 23.5 --xgfit 23.1 23.3 \
    --xgfit 2.6 3.6 --xgfit 2.9 3.4 \
    --xgfit 3.6 4


# indium
# K alpha: 24.2097 24.0020
# K beta: 27.2759
# L alpha: 3.28694 3.27929 (detected)
# L beta: 3.48721 3.71381 (can't resolve)
# L gamma: 3.92081
python find_peaks.py \
    --fn files/spectrum_in.txt \
    --bg files/generator_background.txt \
    --cc 0.02241310493166304,0.038446520796036054 \
    --title "Indium Spectrum" \
    --xrange 0,30 \
    --subtractbg \
    --xgfit 2.8 4 --xgfit 2.9 4


# zirconium
# K alpha: 15.7751 15.6909 (detected)
# K beta: 17.6678 (can't resolve)
# L alpha: 2.04236 2.0399 (detected)
# L beta: 2.1244 2.2194 (can't resolve)
# L gamma: 2.3027
python find_peaks.py \
    --fn files/spectrum_zr.txt \
    --bg files/generator_background.txt \
    --cc 0.02241310493166304,0.038446520796036054 \
    --title "Zirconium Spectrum" \
    --xrange 0,30 \
    --subtractbg \
    --xgfit 15.4 16 --xgfit 15.5 15.9 \
    --xgfit 1.7 2.2 --xgfit 1.8 2.2
