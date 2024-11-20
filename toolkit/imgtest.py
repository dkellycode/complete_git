import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ExifTags

img = Image.open(fd.askopenfilename())
print(img.getexif())

exif = {
    ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in ExifTags.TAGS
}

print(exif)