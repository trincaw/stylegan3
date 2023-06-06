import os
import cv2
import numpy as np
from shutil import move

def is_plain_tshirt(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Find contours in the image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check if the image contains only one contour with a rectangular shape
    if len(contours) < 60:
            return True

    return False

def filter_tshirt_images(input_folder, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(input_folder, filename)

            # Load image using OpenCV
            image = cv2.imread(image_path)

            if image is not None:
                # Check if the image is a plain t-shirt
                if is_plain_tshirt(image):
                    # Move the image to the output folder
                    move(image_path, os.path.join(output_folder, filename))

    print("Image filtering completed!")

# Example usage
input_folder = "C:\\Users\\nico\\Desktop\\input_images"
output_folder = "C:\\Users\\nico\\Desktop\\output_images"

filter_tshirt_images(input_folder, output_folder)
