# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt


m, merr, pt, p = np.genfromtxt(
    'B.txt',
    delimiter=',',
    skip_header=1,
    unpack=True
)
ns, bins = np.histogram(m)
centres = bins[:-1] + (bins[1:] - bins[:-1]) / 2
errs = np.sqrt(ns)
plt.errorbar(centres, ns, yerr=errs, fmt='b.')
plt.savefig('mass2.pdf')
