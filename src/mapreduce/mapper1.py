#!/usr/bin/env python3

import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    try:
        sensor_type = row[5]
        print(f"{sensor_type}\t1")
    except:
        continue