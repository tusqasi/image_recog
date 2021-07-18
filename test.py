import cv2
import pytesseract
import argparse
import numpy as np
from PIL import Image

text = pytesseract.image_to_string(Image.open("test2.png"))

print((text))
