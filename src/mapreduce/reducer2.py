#!/usr/bin/env python3

import sys

current_building = None
current_count = 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    building, count = line.split("\t")
    count = int(count)

    if current_building == building:
        current_count += count
    else:
        if current_building is not None:
            print("{0}\t{1}".format(current_building, current_count))

        current_building = building
        current_count = count

# Output final result
if current_building is not None:
    print("{0}\t{1}".format(current_building, current_count))
