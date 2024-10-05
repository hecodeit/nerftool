import os
import shutil

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

# Example usage
subfolder = 'path/to/subfolder'
parent_folder = 'path/to/parent_folder'
move_and_rename_files(subfolder, parent_folder)