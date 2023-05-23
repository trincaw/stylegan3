#pip install pillow

import os
from PIL import Image

def convert_images(input_folder):
    output_folder = input_folder + "_converted"
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            # Open the image
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)

            # Convert to PNG format
            new_filename = os.path.splitext(filename)[0] + ".png"
            output_path = os.path.join(output_folder, new_filename)
            image.save(output_path, "PNG")

            print(f"Converted {filename} to {new_filename}")

    print("Conversion completed.")

# Example usage:
input_path = "/path/to/input/folder"
convert_images(input_path)