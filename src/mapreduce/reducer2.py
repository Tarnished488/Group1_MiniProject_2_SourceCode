#!/usr/bin/env python3
import sys

current_building = None
current_count = 0
# Add a flag
first_output = True

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    # Add exception handling to prevent split error
    try:
        building, count = line.split("\t")
        count = int(count)
    except ValueError:
        continue

    if current_building == building:
        current_count += count
    else:
        if current_building is not None:
            # Print header before first output
            if first_output:
                print("building,failure_count")
                first_output = False
            # Changed to comma-separated output
            print("{0},{1}".format(current_building, current_count))

        current_building = building
        current_count = count

# Output the final result
if current_building is not None:
    if first_output:
        print("building,failure_count")
    print("{0},{1}".format(current_building, current_count))