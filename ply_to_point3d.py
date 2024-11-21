import plyfile
import numpy as np

# Input and output file paths
input_ply = "pc.ply"  # Replace with your PLY file path
output_points3d = "points3D.txt"

# Default values for COLMAP-specific fields
default_error = 0.0
default_track = []  # Empty track by default

# Function to parse PLY and generate COLMAP's points3D.txt
def convert_ply_to_points3d(input_ply, output_points3d):
    # Load PLY file
    ply_data = plyfile.PlyData.read(input_ply)
    vertices = ply_data['vertex']

    # Extract data
    positions = np.vstack([vertices['x'], vertices['y'], vertices['z']]).T
    if {'red', 'green', 'blue'}.issubset(vertices.data.dtype.names):
        colors = np.vstack([vertices['red'], vertices['green'], vertices['blue']]).T
    else:
        colors = np.zeros_like(positions)  # Default to black if colors are not present

    # Prepare COLMAP points3D data
    with open(output_points3d, "w") as file:
        for point_id, (position, color) in enumerate(zip(positions, colors), start=1):
            x, y, z = position
            r, g, b = color
            error = default_error
            track_str = " ".join(
                f"{image_id} {point2d_idx}" for image_id, point2d_idx in default_track
            )
            file.write(f"{point_id} {x} {y} {z} {r} {g} {b} {error} {track_str}\n")

    print(f"Converted {len(positions)} points from PLY to points3D.txt format.")

# Run the conversion
convert_ply_to_points3d(input_ply, output_points3d)