#!/usr/bin/env python3

import sys
import csv

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    fields = next(csv.reader([line]))

    if fields[0] == "age":
        continue

    try:
        x = float(fields[3])
        y = float(fields[9])
    except (IndexError, ValueError):
        continue

    print("ALL\t{},{}".format(x, y))