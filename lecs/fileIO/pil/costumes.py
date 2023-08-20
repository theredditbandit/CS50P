import sys

from PIL import Image

images = []

# This loop iterates over the command line arguments
for arg in sys.argv[1:]: # not including the first element in sys.argv since it's the name of the file itself   
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif",save_all=True,append_images=[images[1]],duration=200,loop=0
)
