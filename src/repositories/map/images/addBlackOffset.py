import os
import cv2
import numpy as np
from PIL import Image, ImageOps


# Get the directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the border size
border_size = 100

# List all PNG files in the script's directory
png_files = [file for file in os.listdir(script_directory) if file.endswith('.png')]

for file_name in png_files:
    # Read the image with an alpha channel
    image_path = os.path.join(script_directory, file_name)

    # Save the new image
    output_path = os.path.join(script_directory, f"{file_name}")
    # cv2.imwrite(output_path, bordered_image, [cv2.IMWRITE_PNG_COMPRESSION, 0])  # Ensure PNG format and set compression to 0 for grayscale

    ImageOps.expand(Image.open(image_path),border=100,fill='black').save(output_path)

print("Borders added to all PNG files.")
