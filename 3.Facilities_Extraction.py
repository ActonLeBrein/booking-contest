from string import *

N = int(raw_input())
properties = []
for _ in xrange(N):
    d = raw_input()
    properties.append(d)
description = raw_input().lower()

match = []
for i in properties:
    if find(description,i.lower()) >= 0:
        match.append(i)
for j in sorted(match):
    print j