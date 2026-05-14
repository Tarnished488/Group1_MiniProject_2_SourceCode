#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()

    # Skip empty lines
    if not line:
        continue

    fields = line.split(",")

    # Skip invalid rows
    if len(fields) != 10:
        continue

    building = fields[2]
    status = fields[8]

    # Only WARNING and ERROR
    if status == "WARNING" or status == "ERROR":
        print(f"{building}\t1")