import sys, csv

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    fields = next(csv.reader([line]))
    if fields[0] == "age":
        continue
    try:
        gender = fields[1]
        usage = float(fields[3])
    except (IndexError, ValueError):
        continue
    print("{}\t{}".format(gender, usage))
