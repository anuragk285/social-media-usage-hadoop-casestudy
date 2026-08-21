#!/usr/bin/env python3

import sys

def emit(key, total, count):
    if key is not None and count > 0:
       print("{}\t{:.3f}\t{}".format(key, total/count, count))

current_key = None
total = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    key, value = line.split("\t", 1)
    value = float(value)

    if key == current_key:
        total += value
        count += 1
    else:
        emit(current_key, total, count)
        current_key = key
        total = value
        count = 1

emit(current_key, total, count)