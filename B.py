# coding: utf-8
from collections import namedtuple
import matplotlib.pyplot as plt


B = namedtuple('B', ['m', 'merr', 'pt', 'p'])
bs = []
with open('B.txt') as f:
    for line in f.readlines()[1:]:
        line = line.strip()
        values = line.split(',')
        actual_values = [float(v) for v in values]
        b = B(*actual_values)
        bs.append(b)

masses = [b.m for b in bs]
plt.hist(masses)
plt.savefig('mass.pdf')
