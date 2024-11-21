import csv
import numpy as np
from math import radians, cos, sin
from pathlib import Path

# Function to convert heading, pitch, roll to quaternion
def euler_to_quaternion(heading, pitch, roll):
    h, p, r = radians(heading), radians(pitch), radians(roll)
    qw = cos(h / 2) * cos(p / 2) * cos(r / 2) + sin(h / 2) * sin(p / 2) * sin(r / 2)
    qx = sin(h / 2) * cos(p / 2) * cos(r / 2) - cos(h / 2) * sin(p / 2) * sin(r / 2)
    qy = cos(h / 2) * sin(p / 2) * cos(r / 2) + sin(h / 2) * cos(p / 2) * sin(r / 2)
    qz = cos(h / 2) * cos(p / 2) * sin(r / 2) - sin(h / 2) * sin(p / 2) * cos(r / 2)
    return qw, qx, qy, qz

# File paths
input_csv = "realitycapture_export.csv"
output_cameras = "cameras.txt"
output_images = "images.txt"

# Constants
camera_id = 1
camera_model = "OPENCV_FISHEYE"  # Fisheye camera model in COLMAP
image_width = 4000  # Replace with actual value
image_height = 3000  # Replace with actual value

# Initialize outputs
image_id = 1
cameras = []
images = []

# Read RealityCapture CSV
with open(input_csv, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Extract intrinsics (assumed shared across all images)
        if image_id == 1:  # Write only once
            fx = float(row["f"])
            fy = float(row["f"])  # Assuming square pixels
            cx = float(row["px"])
            cy = float(row["py"])
            k1 = float(row["k1"])
            k2 = float(row["k2"])
            k3 = float(row["k3"])
            k4 = float(row["k4"])
            cameras.append(
                f"{camera_id} {camera_model} {image_width} {image_height} {fx} {fy} {cx} {cy} {k1} {k2} {k3} {k4}"
            )

        # Extract extrinsics
        tx, ty, tz = float(row["x"]), float(row["y"]), float(row["alt"])
        heading, pitch, roll = float(row["heading"]), float(row["pitch"]), float(row["roll"])
        qw, qx, qy, qz = euler_to_quaternion(heading, pitch, roll)

        # Append image data
        images.append(f"{image_id} {qw} {qx} {qy} {qz} {tx} {ty} {tz} {camera_id} {row['#name']}")
        image_id += 1

# Write Cameras.txt
with open(output_cameras, "w") as cam_file:
    cam_file.write("\n".join(cameras))

# Write Images.txt
with open(output_images, "w") as img_file:
    img_file.write("\n".join(images))

print(f"Conversion complete. Files saved as '{output_cameras}' and '{output_images}'.")