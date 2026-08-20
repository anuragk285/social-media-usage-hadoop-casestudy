#!/usr/bin/env python3

import sys
import math

n = 0
sum_x = 0.0
sum_y = 0.0
sum_xy = 0.0
sum_x2 = 0.0
sum_y2 = 0.0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    _, pair = line.split("\t", 1)

    x_str, y_str = pair.split(",")

    x = float(x_str)
    y = float(y_str)

    n += 1
    sum_x += x
    sum_y += y
    sum_xy += x * y
    sum_x2 += x * x
    sum_y2 += y * y

if n > 1:
    numerator = n * sum_xy - sum_x * sum_y

    denominator = math.sqrt(
        (n * sum_x2 - sum_x ** 2) *
        (n * sum_y2 - sum_y ** 2)
    )

    r = numerator / denominator if denominator != 0 else 0

    print("n={}\tpearson_r={:.4f}".format(n, r))