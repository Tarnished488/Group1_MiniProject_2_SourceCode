#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    try:
        # Index 1 corresponds to the 2nd column: device_id
        if len(row) > 1:
            device_id = row[1].strip()

            # Skip header and empty values
            if device_id == "device_id" or not device_id:
                continue

            # Mapper output: device_id -> 1 event
            print("{0}\t1".format(device_id))
    except:
        continue
