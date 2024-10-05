import os
import shutil
import argparse

def move_and_rename_files(subfolder, parent_folder):
    # Get the name of the subfolder
    subfolder_name = os.path.basename(subfolder)
    
    # Iterate over all files in the subfolder
    for filename in os.listdir(subfolder):
        # Construct the full file path
        file_path = os.path.join(subfolder, filename)
        
        # Check if it is a file
        if os.path.isfile(file_path):
            # Construct the new file name
            new_filename = f"{subfolder_name}_{filename}"
            new_file_path = os.path.join(parent_folder, new_filename)
            
            # Move the file to the parent folder with the new name
            shutil.move(file_path, new_file_path)
            print(f"Moved: {file_path} to {new_file_path}")

# Set up argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Move and rename files from a subfolder to a parent folder.")
    parser.add_argument('subfolder', type=str, help="Path to the subfolder containing files to move.")
    parser.add_argument('parent_folder', type=str, help="Path to the parent folder where files will be moved.")

    # Parse the arguments
    args = parser.parse_args()

    # Call the function with parsed arguments
    move_and_rename_files(args.subfolder, args.parent_folder)
