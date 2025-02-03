import os
from PIL import Image

folder = "dataset"
for filename in os.listdir(folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img = Image.open(os.path.join(folder, filename))
        img = img.resize((64, 64))
        img.save(os.path.join(folder, filename))
print("Complete")
