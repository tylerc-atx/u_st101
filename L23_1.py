import random
from math import sqrt

def mean(data):
    return sum(data)/len(data)

def variance(data):
    mu=mean(data)
    return sum([(x-mu)**2 for x in data])/len(data)

def stddev(data):
    return sqrt(variance(data))

weight=[80.,85,200,85,69,65,68,66,85,72,85,82,65,105,75,80,
    70,74,72,70,80,60,80,75,80,78,63,88.65,90,89,91,1.00E+22,
    75,75,90,80,75,-1.00E+22,-1.00E+22,-1.00E+22,86.54,67,70,92,70,76,81,93,
    70,85,75,76,79,89,80,73.6,80,80,120,80,70,110,65,80,
    250,80,85,81,80,85,80,90,85,85,82,83,80,160,75,75,
    80,85,90,80,89,70,90,100,70,80,77,95,120,250,60]

print mean(weight)


def calculate_weight(data, z):
    """Returns the standard score for z deviations"""
    # remove outliers
    data_w = data
    data_w.sort()
    quartile_size = (len(data_w) - 3) / 4
    list_mid_quarts = data_w[(quartile_size + 1):\
                           ((quartile_size * 3) + 4)]
    # extract data between lower and upper quartile

    mle_w = mean(list_mid_quarts)
    # fit Gaussian using MLE TYLER: No need for gaussian continuous..

    stddev_w = stddev(list_mid_quarts)

    x = (stddev_w * z) + mle_w
    # compute x that corresponds to standard score z
    return x


print calculate_weight(weight, -2.)
