#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    try:
        if len(row) > 8:
            building = row[2]
            status = row[8]
            if status == "WARNING" or status == "ERROR":
                print("{}\t1".format(building))
    except:
        continue