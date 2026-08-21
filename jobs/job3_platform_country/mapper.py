import sys
import csv

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    try:
        row = next(csv.reader([line]))

        # Skip header
        if row[0].strip().lower() == "age":
            continue

        # Dataset columns:
        # 0 = age
        # 1 = gender
        # 2 = country
        # 3 = daily_usage_hours
        # 4 = primary_platform

        country = row[2].strip()
        daily_usage_hours = float(row[3].strip())
        platform = row[4].strip()

        if not country or not platform:
            continue

        print(f"{country}\t{platform}\t{daily_usage_hours}")

    except (ValueError, IndexError):
        continue