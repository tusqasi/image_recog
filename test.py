import cv2
import pytesseract
import argparse
import numpy as np
from PIL import Image

# This is the path of image on which character recognition is run
image_path = "./test2.png"

# `text` variable will now be assigned with the text on the image
text = pytesseract.image_to_string(Image.open(image_path))


print((text))
