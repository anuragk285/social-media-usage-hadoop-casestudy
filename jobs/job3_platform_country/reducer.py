import sys
from collections import defaultdict

current_country = None
platform_data = defaultdict(lambda: [0, 0.0])


def process_country(country, data):
    if not country or not data:
        return

    # Find maximum user count
    max_count = max(values[0] for values in data.values())

    # Platforms tied for maximum count
    candidates = [
        platform
        for platform, values in data.items()
        if values[0] == max_count
    ]

    # If there is a tie, choose the platform
    # with the highest average daily usage hours.
    if len(candidates) > 1:

        winner = max(
            candidates,
            key=lambda platform: (
                data[platform][1] / data[platform][0],
                platform
            )
        )

    else:
        winner = candidates[0]

    count = data[winner][0]

    # Average usage is used only for tie-breaking.
    # It is not included in the final output.
    print(f"{country:<15}{winner:<25}{count:>10}")


for line in sys.stdin:

    line = line.strip()

    if not line:
        continue

    parts = line.split("\t")

    if len(parts) != 3:
        continue

    country = parts[0].strip()
    platform = parts[1].strip()

    try:
        daily_usage_hours = float(parts[2].strip())
    except ValueError:
        continue

    if not country or not platform:
        continue

    # Country changed → process previous country
    if current_country is not None and country != current_country:
        process_country(current_country, platform_data)
        platform_data.clear()

    current_country = country

    # Count users
    platform_data[platform][0] += 1

    # Add daily usage hours
    platform_data[platform][1] += daily_usage_hours


# Process final country
if current_country is not None:
    process_country(current_country, platform_data)