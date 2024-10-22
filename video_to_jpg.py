import argparse
import os
import subprocess

def convert_mp4_to_jpg(input_file, output_pattern):
    ffmpeg_command = [
        "ffmpeg",
        "-i", input_file,
        "-vf", "fps=1",
        "-qscale:v", "2",
        output_pattern
    ]
    
    result = subprocess.run(ffmpeg_command, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(f"Conversion successful: {result.stdout}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert MP4 to high-quality JPG images.")
    parser.add_argument("input_file", help="Path to the input MP4 file.")
    parser.add_argument("output_pattern", help="Output file pattern for JPG images (e.g., output_%04d.jpg).")
    
    args = parser.parse_args()
    
    if not os.path.isfile(args.input_file):
        print(f"Error: Input file '{args.input_file}' does not exist.")
    else:
        convert_mp4_to_jpg(args.input_file, args.output_pattern)