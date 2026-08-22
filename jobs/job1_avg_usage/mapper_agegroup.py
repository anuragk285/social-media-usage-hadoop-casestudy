import sys, csv

def age_group(age):
    if age < 18: return "Under18"
    elif age < 25: return "18-24"
    elif age < 35: return "25-34"
    elif age < 45: return "35-44"
    else: return "45+"

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    fields = next(csv.reader([line]))
    if fields[0] == "age":
        continue
    try:
        age = int(float(fields[0]))
        usage = float(fields[3])
    except (IndexError, ValueError):
        continue
    print("{}\t{}".format(age_group(age), usage))
