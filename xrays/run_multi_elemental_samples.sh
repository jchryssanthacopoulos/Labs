#!/bin/bash


# US quarter
python find_peaks.py \
    --fn files/spectrum_usquarter.txt \
    --cc 0.0224184909253429,0.0753904723122858 \
    --xrange 2,16 \
    --height 15 \
    --threshold 5 \
    --xgfit 7.2 7.7 --xgfit 7.8 8.4
