import os
import random
from PIL import Image

# Function to generate a random image
def generate_random_image(width, height):
    # Create a blank image with the specified size
    img = Image.new("RGB", (width, height), (0, 0, 0))

    # Get the image's pixel data
    pixels = img.load()

    # Iterate over each pixel and set its color to a random value
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    return img

# Get the number of images to generate
num_images = int(input("Enter the number of images to generate: "))

# Get the image size
width = int(input("Enter the image width: "))
height = int(input("Enter the image height: "))

# Generate the images
for i in range(num_images):
    # Create the image
    img = generate_random_image(width, height)

    # Save the image to file
    img.save("random_image_{}.png".format(i))

print("{} random images have been generated with the specified size".format(num_images))
