import ray
import pandas as pd
import numpy as np
import os

# Initialize Ray
ray.init()

print("Ray started successfully!")

# Read dataset
access_key = "AKIAZP6KVLUWB7L3CAKZ"
secret_key = "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"
s3_uri = "s3://smart-campus-iot-logs-group1/Comp3006J MiniProject 2 Dataset.csv" 

df = pd.read_csv(
    s3_uri, 
    storage_options={
        "key": access_key,
        "secret": secret_key
    }
)

print(f"Dataset loaded: {df.shape[0]} rows")

# Convert numeric columns safely
df["battery_level"] = pd.to_numeric(df["battery_level"], errors="coerce")
df["value"] = pd.to_numeric(df["value"], errors="coerce")

# Split dataset into chunks
chunks = np.array_split(df, 4)

print(f"Dataset split into {len(chunks)} chunks")


@ray.remote
def process_chunk(chunk):

    low_battery_list = []

    error_counts = {}

    high_temp_counts = {}

    # Process each row
    for _, row in chunk.iterrows():

        device_id = row["device_id"]
        building = row["building"]

        key = (device_id, building)

        # Condition 1: Low battery
        if row["battery_level"] < 20:

            low_battery_list.append(
                [device_id, building, "low battery"]
            )

        # Count ERROR records
        if row["status"] == "ERROR":

            if key not in error_counts:
                error_counts[key] = 0

            error_counts[key] += 1

        # Count high temperature records
        if (
            row["sensor_type"] == "temperature"
            and row["value"] > 32
        ):

            if key not in high_temp_counts:
                high_temp_counts[key] = 0

            high_temp_counts[key] += 1

    return {
        "low_battery": low_battery_list,
        "error_counts": error_counts,
        "high_temp_counts": high_temp_counts
    }


print("Starting parallel Ray tasks...")

# Launch Ray tasks
tasks = [process_chunk.remote(chunk) for chunk in chunks]

# Collect results
results = ray.get(tasks)

print("Parallel processing finished!")

# Final abnormal result list
final_results = []

# Global count dictionaries
global_error_counts = {}

global_high_temp_counts = {}

# Merge all chunk results
for result in results:

    # Merge low battery results directly
    final_results.extend(result["low_battery"])

    # Merge ERROR counts
    for key, count in result["error_counts"].items():

        if key not in global_error_counts:
            global_error_counts[key] = 0

        global_error_counts[key] += count

    # Merge high temperature counts
    for key, count in result["high_temp_counts"].items():

        if key not in global_high_temp_counts:
            global_high_temp_counts[key] = 0

        global_high_temp_counts[key] += count


# Check repeated errors globally
for (device_id, building), count in global_error_counts.items():

    if count >= 3:

        final_results.append(
            [device_id, building, "repeated errors"]
        )


# Check repeated high temperature globally
for (device_id, building), count in global_high_temp_counts.items():

    if count >= 3:

        final_results.append(
            [device_id, building, "repeated high temperature"]
        )


# Convert to DataFrame
final_df = pd.DataFrame(
    final_results,
    columns=["device_id", "building", "reason"]
)

# Remove duplicates
final_df = final_df.drop_duplicates()

# Create output directory
os.makedirs("output", exist_ok=True)

# Save output
output_path = "output/abnormal_devices.csv"

final_df.to_csv(output_path, index=False)

print("\nAbnormal devices detected:")

print(final_df.head(20))

print(f"\nResults saved to: {output_path}")

# Shutdown Ray
ray.shutdown()