#!/usr/bin/env python3
import sys
import csv

# Use the csv module to handle commas more robustly
reader = csv.reader(sys.stdin)

for row in reader:
    try:
        # Index 6 corresponds to the 7th column: event_type
        if len(row) > 6:
            event_type = row[6].strip()
            
            # Key filter: skip header text and empty values
            if event_type == "event_type" or not event_type:
                continue
            
            # Output to reducer using tab separation
            print("{0}\t1".format(event_type))
    except:
        # Fault tolerance: skip malformed rows
        continue