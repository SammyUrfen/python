import os
import json
from PIL import Image

def convert_json_to_box_all(json_dir, img_dir, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Get sorted list of JSON files and corresponding images
    json_files = sorted([f for f in os.listdir(json_dir) if f.endswith('.json')])
    img_files = sorted([f for f in os.listdir(img_dir) if f.endswith(('.png', '.jpg', '.jpeg'))])

    for json_file, img_file in zip(json_files, img_files):
        # Paths to current JSON and image
        json_path = os.path.join(json_dir, json_file)
        img_path = os.path.join(img_dir, img_file)

        # Open the image to get its dimensions
        with Image.open(img_path) as img:
            image_width, image_height = img.size

        # Path for the output .box file
        box_file = os.path.join(output_dir, os.path.splitext(json_file)[0] + '.box')

        # Convert JSON to .box format
        with open(json_path, 'r') as f:
            data = json.load(f)

        with open(box_file, 'w') as f:
            for obj in data['shapes']:
                label = obj['label']
                points = obj['points']
                x1, y1 = points[0]
                x2, y2 = points[1]

                # Flip the y-coordinates (Tesseract uses bottom-up coordinates)
                y1, y2 = image_height - y1, image_height - y2

                # Ensure y1 < y2
                y1, y2 = min(y1, y2), max(y1, y2)

                # Write the .box format line
                f.write(f"{label} {int(x1)} {int(y1)} {int(x2)} {int(y2)} 0\n")

        print(f"Processed {json_file} -> {box_file}")

# Directories
json_dir = 'labels'       # Path to LabelImg JSON files
img_dir = 'images'        # Path to corresponding images
output_dir = 'box_labels' # Path to store the .box files

# Run the conversion
convert_json_to_box_all(json_dir, img_dir, output_dir)
