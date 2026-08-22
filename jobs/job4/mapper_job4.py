#!/usr/bin/env python3
import sys, csv

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    fields = next(csv.reader([line]))
    if fields[0] == "age":  # skip header
        continue
    try:
        platform = fields[4]     # primary_platform
        addiction = fields[10]   # addiction_level
    except IndexError:
        continue
    print("{}|{}\t1".format(platform, addiction))
