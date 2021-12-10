#!/bin/bash


######################
# Calibrate Position #
######################

# UP TAC
# m = 0.00010914992943457062
# b = -0.7429201535521206
# m_2 = 0.00011394037727937724
# b_2 = -0.8050489259980036
python calibrate_time.py \
    --channel 7.72259e+03,1.68843e+04 \
    --time 0.1,1.1 \
    --channel_sigma 3.81497e+01,3.88968e+01

# lower bound
python calibrate_time.py \
    --channel 7760.7397,16845.4032 \
    --time 0.1,1.1 \
    --channel_sigma 3.81497e+01,3.88968e+01
# upper bound
python calibrate_time.py \
    --channel 7684.4403,16923.196799999998 \
    --time 0.1,1.1 \
    --channel_sigma 3.81497e+01,3.88968e+01

# tracker peak 1
# constant = 4.01958e+01 +/- 1.16787e+00
# mean = 7.72259e+03 +/- 3.81497e+01
# sigma = 1.19187e+03 +/- 4.74089e+01

# tracker peak 2
# constant = 3.64147e+01 +/- 1.05588e+00
# mean = 1.68843e+04 +/- 3.88968e+01
# sigma = 1.26362e+03 +/- 4.34499e+01

# DOWN TAC
# m = 0.0001066245854969239
# b = -1.1976638553317625
python calibrate_time.py \
    --channel 1.21704e+04,2.15491e+04 \
    --time 0.1,1.1 \
    --channel_sigma 5.84010e+02,5.80248e+02

# tracker peak 1
# constant = 8.55777e+01 +/- 2.35292e+00
# mean = 1.21704e+04 +/- 1.46906e+01
# sigma = 5.84010e+02 +/- 1.18982e+01

# tracker peak 2
# constant = 8.56930e+01 +/- 2.36888e+00
# mean = 2.15491e+04 +/- 1.39606e+01
# sigma = 5.80248e+02 +/- 1.10986e+01
