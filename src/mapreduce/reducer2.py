#!/usr/bin/env python3
import sys

current_building = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    building, count = line.split("\t")

    if building == "_header_building_stats":
        print("building,failure_count")
        continue

    try:
        count = int(count)
    except ValueError:
        continue

    if current_building == building:
        current_count += count
    else:
        if current_building is not None:
            print("{0},{1}".format(current_building, current_count))

        current_building = building
        current_count = count

if current_building is not None:
    print("{0},{1}".format(current_building, current_count))