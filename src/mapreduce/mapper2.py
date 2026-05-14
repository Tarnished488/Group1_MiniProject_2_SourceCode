#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    if "timestamp" in line:
        continue
    fields = line.split(",")
    if len(fields) != 10:
        continue
    building = fields[2].strip()
    status = fields[8].strip()
    if status == "WARNING" or status == "ERROR":
        print("{0}\t1".format(building))