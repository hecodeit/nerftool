import argparse
import subprocess
import os
import math

def run_colmap(project_path):
    image_path = os.path.join(project_path, 'input')
    database_path = os.path.join(project_path, 'project.db')
    output_path = os.path.join(project_path, 'sparse')
    vocab_tree_path = 'vocab_tree_flickr100K_words32K.bin'  # Local file for vocab tree path

    # Ensure output_path is a directory
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    elif not os.path.isdir(output_path):
        raise ValueError(f"The output_path '{output_path}' is not a directory.")

    # Count the number of image files in image_path
    num_images = len([name for name in os.listdir(image_path) if os.path.isfile(os.path.join(image_path, name))])
    min_model_size = math.ceil(0.8 * num_images)

    # Feature extractor
    subprocess.run([
        'colmap', 'feature_extractor',
        '--database_path', database_path,
        '--image_path', image_path,
        '--ImageReader.single_camera', '1',
        '--ImageReader.camera_model', 'OPENCV_FISHEYE',
        '--SiftExtraction.use_gpu', '1'
    ])

    # Vocab tree matcher
    subprocess.run([
        'colmap', 'vocab_tree_matcher',
        '--database_path', database_path,
        '--VocabTreeMatching.vocab_tree_path', vocab_tree_path,
        '--SiftMatching.use_gpu', '1'
    ])

    # Mapper
    subprocess.run([
        'colmap', 'mapper',
        '--database_path', database_path,
        '--image_path', image_path,
        '--output_path', output_path,
        '--Mapper.min_model_size', str(min_model_size)
    ])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run COLMAP commands with input arguments.')
    parser.add_argument('project_path', type=str, help='Path to the project directory.')

    args = parser.parse_args()

    run_colmap(args.project_path)