#!/usr/bin/env python3
import sys, csv

def usage_bucket(hours):
    if hours < 2: return "0-2h"
    elif hours < 4: return "2-4h"
    elif hours < 6: return "4-6h"
    elif hours < 8: return "6-8h"
    else: return "8h+"

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    fields = next(csv.reader([line]))
    if fields[0] == "age":
        continue
    try:
        usage = float(fields[3])
        mental_health = float(fields[9])
    except (IndexError, ValueError):
        continue
    print("{}\t{}".format(usage_bucket(usage),mental_health))