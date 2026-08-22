import sys, csv

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    fields = next(csv.reader([line]))
    if fields[0] == "age":
        continue
    try:
        country = fields[2]
        usage = float(fields[3])
    except (IndexError, ValueError):
        continue
    print("{}\t{}".format(country, usage))
