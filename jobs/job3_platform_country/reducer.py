#!/usr/bin/env python3

import sys
from collections import defaultdict


def emit_result(country, platform_counts):
    if not country or not platform_counts:
        return

    # Find the highest number of users
    max_count = max(platform_counts.values())

    # Find all platforms having the highest count
    winners = [
        platform
        for platform, count in platform_counts.items()
        if count == max_count
    ]

    # If there is a tie, choose alphabetically first
    winner = min(winners)

    # Output:
    # Country    Most_Popular_Platform    User_Count
    print(f"{country}\t{winner}\t{max_count}")


def main():

    current_country = None
    platform_counts = defaultdict(int)

    for line in sys.stdin:

        line = line.strip()

        if not line:
            continue

        # Mapper output format:
        # country<TAB>platform
        parts = line.split("\t", 1)

        if len(parts) != 2:
            continue

        country = parts[0].strip()
        platform = parts[1].strip()

        if not country or not platform:
            continue

        # When we reach a new country,
        # finish processing the previous country.
        if current_country is not None and country != current_country:

            emit_result(current_country, platform_counts)

            platform_counts.clear()

        current_country = country

        # Count this platform for the current country
        platform_counts[platform] += 1

    # Process the last country
    if current_country is not None:
        emit_result(current_country, platform_counts)


if __name__ == "__main__":
    main()