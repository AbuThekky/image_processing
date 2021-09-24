import sys
import os
from PIL import Image

# GRAB FIRST AND SECOND ARGUMENT
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# CHECK IS NEW/ EXISTS, IF NOT CREATED
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{filename}")
    clean_name = os.path.splitext(filename)
    img.save(f"{output_folder}{filename}.png", "png")
    print("all done")
