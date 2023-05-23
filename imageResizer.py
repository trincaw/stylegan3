
import os
from PIL import Image
import cv2

# Set the paths for the input and output directories
input_dir = "/home/ntrinca/img"
output_dir = "/home/ntrinca/resized_img"


# Ensure that the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate over the files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg"):
        # Load the image using OpenCV
        image_path = os.path.join(input_dir, filename)
        image = cv2.imread(image_path)

        # Resize the image to 1024x1024
        resized_image = cv2.resize(image, (1024, 1024))

        # Convert the image to PIL format
        pil_image = Image.fromarray(resized_image)

        # Change the format to PNG and save with compression level
        output_filename = os.path.splitext(filename)[0] + ".png"
        output_path = os.path.join(output_dir, output_filename)
        pil_image.save(output_path, format='PNG')
