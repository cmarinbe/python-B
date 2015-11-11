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
widths = (bins[1:] - bins[:-1]) / 2
centres = bins[:-1] + widths
errs = 100 * np.sqrt(ns)
plt.errorbar(centres, ns, xerr=widths, yerr=errs, fmt='b.')
plt.xlabel(r'$m(B\to K^{*0}\mu\mu)$ [MeV/c$^2$]')
plt.ylabel('#events')
plt.savefig('mass2.pdf')
