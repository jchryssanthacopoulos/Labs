#!/bin/bash


python find_peaks.py \
    --fn files/generator_background.txt \
    --cc 0.02241310493166304,0.038446520796036054 \
    --title "Generator Background Spectrum" \
    --xrange 0,20 \
    --xgfit 2.35 2.85 --xgfit 2.4 2.8 \
    --xgfit 2.6 3.3 --xgfit 2.7 3.2 \
    --xgfit 6.5 7.3 --xgfit 6.7 7.1 \
    --xgfit 7.3 8.6 --xgfit 7.6 8.3 \
    --xgfit 8.5 10 --xgfit 8.75 9.5 \
    --xgfit 10 11 --xgfit 10.2 10.8 \
    --xgfit 12 13.2 --xgfit 12.4 12.9
