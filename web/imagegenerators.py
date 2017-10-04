import PIL
from PIL import Image
from django.conf import settings
from imagekit import ImageSpec, register
from pilkit.processors import AddBorder


def add_watermark(image, watermark):
    rgba_image = image
    rgba_watermark = watermark

    image_x, image_y = rgba_image.size
    watermark_x, watermark_y = rgba_watermark.size

    if image_x > image_y:
        escala_y = watermark_y / watermark_x
        nuevo_watermark_x = image_x * 0.3
        nuevo_watermark_y = nuevo_watermark_x * escala_y
    else:
        escala_y = watermark_y / watermark_x
        nuevo_watermark_x = image_x * 0.6
        nuevo_watermark_y = nuevo_watermark_x * escala_y

    new_size = (int(nuevo_watermark_x), int(nuevo_watermark_y))
    rgba_watermark = rgba_watermark.resize(new_size, resample=PIL.Image.ANTIALIAS)

    watermark_x, watermark_y = rgba_watermark.size
    rgba_image.paste(rgba_watermark,
                     ((image_x - watermark_x - int(image_x * 0.05)), (image_y - watermark_y - int(image_y * 0.05))),
                     rgba_watermark)

    return rgba_image


class WatermarkProcessorNormal(object):
    watermark = Image.open(settings.IMAGEKIT_WATERMARK_IMAGE)

    def process(self, image):
        return image


class WatermarkProcessor(object):
    watermark = Image.open(settings.IMAGEKIT_WATERMARK_IMAGE)

    def process(self, image):
        return add_watermark(image, self.watermark)


class WatermarkProcessorOrange(object):
    watermark = Image.open(settings.IMAGEKIT_WATERMARK_IMAGE_ORANGE)

    def process(self, image):
        return add_watermark(image, self.watermark)


class Watermark(ImageSpec):
    processors = [WatermarkProcessor()]
    format = 'PNG'
    options = {'quality': 100}


class WatermarkOrange(ImageSpec):
    processors = [WatermarkProcessorOrange(), AddBorder(thickness=5, color=(237, 107, 0))]
    format = 'PNG'
    options = {'quality': 100}


class Normal(ImageSpec):
    processors = [WatermarkProcessorNormal()]
    format = 'PNG'


register.generator('webpage:watermark', Watermark)
register.generator('webpage:watermark_orange', WatermarkOrange)
register.generator('webpage:normal', Normal)
