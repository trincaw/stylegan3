import os
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error as mse
from skimage.io import imread, imsave
from skimage.color import rgb2gray
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt
from skimage import io


def compare_images(img1_path, img2_path, sigma=1.5):
    img1 = rgb2gray(imread(img1_path))
    img2 = rgb2gray(imread(img2_path))

    # Apply Gaussian filter to the images
    img1_smooth = gaussian_filter(img1, sigma=sigma)
    img2_smooth = gaussian_filter(img2, sigma=sigma)

    # plt.figure()
    # f, axarr = plt.subplots(2,1)
    # plt.axis('off')
    # axarr[0].imshow(img1_smooth, cmap='gray')
    # axarr[1].imshow(img2_smooth, cmap='gray')
    # plt.show()

    # Calculate structural similarity and mean squared error
    similarity = ssim(img1_smooth, img2_smooth, data_range=img1_smooth.max())
    mse_value = mse(img1_smooth, img2_smooth)

    return similarity, mse_value

def process_images(input_folder, filter_folder, output_folder, threshold=0.61):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for input_file in os.listdir(input_folder):
        input_path = os.path.join(input_folder, input_file)
        match_found = False

        for filter_file in os.listdir(filter_folder):
            filter_path = os.path.join(filter_folder, filter_file)

            similarity, mse_value = compare_images(input_path, filter_path)
            if similarity > threshold:
                output_file = os.path.splitext(input_file)[0] + "_filtered.jpg"
                output_path = os.path.join(output_folder, output_file)
                imsave(output_path, imread(input_path))
                print(f"Saved filtered image: {output_file} similarity: {similarity} MSE: {mse_value}")
                match_found = True
                break

        if not match_found:
            print(f"No filter match found for image {input_file} similarity: {similarity} MSE: {mse_value}")

# Set the paths to your input, filter, and output folders
input_folder = "input_images"
filter_folder = "filter_images"
output_folder = "output_images"

process_images(input_folder, filter_folder, output_folder)