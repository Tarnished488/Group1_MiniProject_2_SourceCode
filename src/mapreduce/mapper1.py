#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    try:
        # Index 5 corresponds to the 6th column: sensor_type
        if len(row) > 5:
            sensor_name = row[5].strip()

            if sensor_name == "sensor_type" or not sensor_name:
                continue
            print("{0}\t1".format(sensor_name))
    except:
        continue