import logging
from io import BytesIO

from PIL import Image
from django.core.files.base import ContentFile
from django.db.models.signals import pre_save
from django.dispatch import receiver
from core.models import ItemImage

THUMBNAIL_SIZE = (300, 300)

logger = logging.getLogger(__name__)
# def load_greyscale_image(filename):
#     """
#     Loads an image from the given file and returns a dictionary
#     representing that image.  This also performs conversion to greyscale.
#
#     Invoked as, for example:
#        i = load_greyscale_image("test_images/cat.png")
#     """
#     with open(filename, "rb") as img_handle:
#         img = Image.open(img_handle)
#         img_data = img.getdata()
#         if img.mode.startswith("RGB"):
#             pixels = [
#                 round(0.299 * p[0] + 0.587 * p[1] + 0.114 * p[2]) for p in img_data
#             ]
#         elif img.mode == "LA":
#             pixels = [p[0] for p in img_data]
#         elif img.mode == "L":
#             pixels = list(img_data)
#         else:
#             raise ValueError(f"Unsupported image mode: {img.mode}")
#         width, height = img.size
#         return img
#
#
# def save_greyscale_image(image, filename, mode="PNG"):
#     """
#     Saves the given image to disk or to a file-like object.  If filename is
#     given as a string, the file type will be inferred from the given name.  If
#     filename is given as a file-like object, the file type will be determined
#     by the "mode" parameter.
#     """
#     out = Image.new(mode="L", size=(image["width"], image["height"]))
#     out.putdata(image["pixels"])
#     if isinstance(filename, str):
#         out.save(filename)
#     else:
#         out.save(filename, mode)
#     out.close()


@receiver(pre_save, sender=ItemImage)
def generate_thumbnail(sender, instance, **kwargs):
    logger.info(
        "Generating thumbnail for product %d",
        instance.item.id,
    )
    image = Image.open(instance.item_image)
    image = image.convert("L")
    image.thumbnail(THUMBNAIL_SIZE, Image.DEFAULT_STRATEGY)
    temp_thumb = BytesIO()
    image.save(temp_thumb, "JPEG")
    temp_thumb.seek(0)
    instance.thumbnail.save(
        instance.item_image.name,
        ContentFile(temp_thumb.read()),
        save=False,
    )
    temp_thumb.close()
