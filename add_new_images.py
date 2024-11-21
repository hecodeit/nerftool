import argparse
import subprocess
import os
import shutil

def generate_image_list(new_image_path, new_image_list_path):
    with open(new_image_list_path, 'w') as file:
        for image_name in os.listdir(new_image_path):
            file.write(f"{image_name}\n")

# def copy_images(src_dir, dst_dir):
#     if not os.path.exists(dst_dir):
#         os.makedirs(dst_dir)
#     for item in os.listdir(src_dir):
#         s = os.path.join(src_dir, item)
#         d = os.path.join(dst_dir, item)
#         if os.path.isdir(s):
#             shutil.copytree(s, d, False, None)
#         else:
#             shutil.copy2(s, d)

def add_new_images(old_project, new_project, all_image_path):
    old_database_path = os.path.join(old_project, 'project.db')
    new_database_path = os.path.join(new_project, 'project.db')
    # old_image_path = os.path.join(old_project, 'input')
    new_image_path = os.path.join(new_project, 'input')
    sparse_input_path = os.path.join(old_project, 'sparse')
    new_sparse_output_path = os.path.join(new_project, 'sparse')
    vocab_tree_path = 'vocab_tree_flickr100K_words32K.bin'  # Local file for vocab tree path

    # Generate new image list
    new_image_list_path = os.path.join(new_image_path, 'new_image_list.txt')
    generate_image_list(new_image_path, new_image_list_path)

    # Copy old database to new database
    shutil.copyfile(old_database_path, new_database_path)

    # Copy old project input images to new project all_images
    # copy_images(old_image_path, all_image_path)
    # copy_images(new_image_path, all_image_path)

    # Ensure new_sparse_output_path is a directory
    if not os.path.exists(new_sparse_output_path):
        os.makedirs(new_sparse_output_path)
    elif not os.path.isdir(new_sparse_output_path):
        raise ValueError(f"The new_sparse_output_path '{new_sparse_output_path}' is not a directory.")

    # Feature extractor for new images
    subprocess.run([
        'colmap', 'feature_extractor',
        '--database_path', new_database_path,
        '--ImageReader.existing_camera_id', '1',
        '--image_path', new_image_path,
        '--image_list_path', new_image_list_path
    ])

    # Vocab tree matcher for new images
    subprocess.run([
        'colmap', 'vocab_tree_matcher',
        '--database_path', new_database_path,
        '--VocabTreeMatching.vocab_tree_path', vocab_tree_path,
        '--VocabTreeMatching.match_list_path', new_image_list_path
    ])

    # Mapper for new images
    subprocess.run([
        'colmap', 'mapper',
        '--database_path', new_database_path,
        '--image_path', all_image_path,
        '--input_path', sparse_input_path,
        '--output_path', new_sparse_output_path
    ])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add new images to the old model using COLMAP.')
    parser.add_argument('old_project', type=str, help='Path to the old project directory.')
    parser.add_argument('new_project', type=str, help='Path to the new project directory.')
    parser.add_argument('all_image_path', type=str, help='Path to the directory containing all images (old and new).')

    args = parser.parse_args()

    add_new_images(args.old_project, args.new_project, args.all_image_path)