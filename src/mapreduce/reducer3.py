#!/usr/bin/env python3
import sys

current_device = None
current_count = 0
device_counts = []

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    parts = line.split("\t")
    if len(parts) != 2:
        continue

    device_id, count = parts

    try:
        count = int(count)
    except ValueError:
        continue

    if current_device == device_id:
        current_count += count
    else:
        if current_device is not None:
            device_counts.append((current_device, current_count))

        current_device = device_id
        current_count = count

# Store final device
if current_device is not None:
    device_counts.append((current_device, current_count))

# Sort by count descending, then device_id ascending for stable tie-breaking
top_10 = sorted(device_counts, key=lambda item: (-item[1], item[0]))[:10]

for device_id, count in top_10:
    print("{0}\t{1}".format(device_id, count))
