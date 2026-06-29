import os
import base64

image_b64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="

with open("img/MIGAS.jpeg", "wb") as f:
    f.write(base64.b64decode(image_b64))

print("Image created.")
