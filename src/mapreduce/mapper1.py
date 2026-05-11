#!/usr/bin/env python3
import sys
import csv


reader = csv.reader(sys.stdin)

for row in reader:
    try:
        if len(row) > 5:
            sensor_type = row[5]
            print("{}\t1".format(sensor_type))
    except:
        continue