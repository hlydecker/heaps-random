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
while True:
    try:
        num_images = int(input("How many kawaii images would you like me to generate, desu~? OwO: "))
        if num_images < 1:
            raise ValueError()
        break
    except ValueError:
        print("Nyaa~! Please enter a positive integer value, nya! (´・ω・`)")

# Get the image size
while True:
    try:
        width = int(input("Please enter the width of the kawaii image, nya~ OwO: "))
        height = int(input("Please enter the height of the kawaii image, nya~ OwO: "))
        if width < 1 or height < 1:
            raise ValueError()
        break
    except ValueError:
        print("Oopsie! The image dimensions must be positive integers, nya~ (◕ᴥ◕)")

# Generate the images
for i in range(num_images):
    # Create the image
    img = generate_random_image(width, height)

    # Save the image to file
    filename = "kawaii_{}.png".format(i)
    img.save(filename)
    print("A kawaii image has been generated and saved as {}".format(filename))

print("All done! I hope you enjoy your super cute kawaii images, nya~! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")

