#!/usr/bin/env python3

import sys
import csv

def main():
    reader = csv.reader(sys.stdin)

    for row in reader:

        # Skip empty rows
        if not row:
            continue

        # Skip header
        if row[0].strip().lower() == "age":
            continue

        # Make sure the row has enough columns
        if len(row) < 5:
            continue

        country = row[2].strip()
        platform = row[4].strip()

        # Ignore records with missing country/platform
        if not country or not platform:
            continue

        # Mapper output:
        # country <TAB> platform
        print(f"{country}\t{platform}")


if __name__ == "__main__":
    main()