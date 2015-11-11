# coding: utf-8

import re

def clean_name(name):
    return name.replace('TimingAuditor.TIMER', '').replace('INFO', '').strip()

with open('log.log') as f:
    lines = f.readlines()
    l1 = [l.strip() for l in lines if l.startswith('TimingAuditor.TIMER')]
    l2 = [l for l in l1 if '|' in l]
    l3 = [l.split('|') for l in l2]
    l4 = [[x.strip() for x in l] for l in l3]
    l5 = [(l[0], float(l[1])) for l in l4[1:]]
    ls = [(clean_name(l[0]), l[1]) for l in l5]
print(ls)

pat = r'TimingAuditor\.TIMER\s+INFO\s+(\w+)\s+\|\s+([\d\.]+)'
with open('log.log') as f:
    matches = [re.match(pat, line) for line in f.readlines()]
    matches = [m.groups() for m in matches if m is not None]
    res = [(m[0], float(m[1])) for m in matches]
print res
