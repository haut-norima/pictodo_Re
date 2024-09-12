# todo/utils.py
from PIL import Image
from django.core.files.base import ContentFile
import io
import os


def resize_image(image, height):
    img = Image.open(image)
    aspect_ratio = img.width / img.height
    new_width = int(height * aspect_ratio)

    resized_img = img.resize((new_width, height), Image.ANTIALIAS)

    # Save the image to a BytesIO object
    img_io = io.BytesIO()
    resized_img.save(img_io, format=img.format)

    # Correctly update the file name
    base, ext = os.path.splitext(image.name)
    new_name = f"{base}_resized{ext}"

    img_content = ContentFile(img_io.getvalue(), name=new_name)

    return img_content