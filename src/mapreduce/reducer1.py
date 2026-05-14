#!/usr/bin/env python3
import sys

current_key = None
current_count = 0
# Add a flag to ensure the header is printed only once
first_output = True

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split("\t")
    if len(parts) != 2:
        continue
        
    key, value = parts
    try:
        value = int(value)
    except ValueError:
        continue

    if current_key == key:
        current_count += value
    else:
        if current_key:
            # Print header before first output
            if first_output:
                print("sensor_type,count")
                first_output = False
            # Changed to comma-separated output
            print("{0},{1}".format(current_key, current_count))
        current_key = key
        current_count = value

if current_key:
    if first_output:
        print("sensor_type,count")
    print("{0},{1}".format(current_key, current_count))