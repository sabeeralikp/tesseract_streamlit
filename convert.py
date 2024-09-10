import pytesseract
from pdf2image import convert_from_path
from pytesseract import image_to_string
import numpy as np

images = convert_from_path(
    "/home/icfoss/Sabeerali/Computer Science/11th Std MM Computer Science Vol-2.pdf"
)
print("images converted")
with open("textbook.txt", "a") as f:
    for i in range(len(images)):
        print(i, "/", len(images))
        f.write(image_to_string(images[i], lang="mal+eng"))

# text = ""

# for image in images:
#     image = np.array(image)
#     text += pytesseract.image_to_string(image, lang="mal+eng")

# with open("textbook.txt", "a") as f:
#     f.write(text)
