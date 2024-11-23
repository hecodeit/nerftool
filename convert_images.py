def convert_images_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        lines = infile.readlines()
        for i in range(len(lines)):
            line = lines[i].strip()
            if line.startswith('#') or line.startswith('Number of images'):
                outfile.write(line + '\n')
                continue

            if i % 2 == 0:  # Process the first line of each image
                parts = line.split()
                if len(parts) == 10:
                    parts[8] = '1'  # Change CAMERA_ID to 1
                    parts[9] = parts[9].replace('.jpg', '.JPG')  # Change .jpg to .JPG
                    outfile.write(' '.join(parts) + '\n')
            else:  # Process the second line of each image
                outfile.write(line + '\n')

if __name__ == "__main__":
    input_file = 'images.txt'
    output_file = 'converted_images.txt'
    convert_images_file(input_file, output_file)