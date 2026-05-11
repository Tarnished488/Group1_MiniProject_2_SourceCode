#!/usr/bin/env python3
import sys

current_key = None
current_count = 0

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
            print("{}\t{}".format(current_key, current_count))
        current_key = key
        current_count = value

if current_key:
    print("{}\t{}".format(current_key, current_count))