import sys
import csv

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    try:
        row = next(csv.reader([line]))

        if row[0].strip().lower() == "age":
            continue

        country = row[2].strip()
        daily_usage_hours = float(row[3].strip())
        platform = row[4].strip()

        if not country or not platform:
            continue

        print(f"{country}\t{platform}\t{daily_usage_hours}")

    except (ValueError, IndexError):
        continue