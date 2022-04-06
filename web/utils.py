import re
from django.utils.text import slugify


def get_image_name(clase, filename):
    split_filename = filename.split(".")
    file_extention = split_filename[-1]
    filename_without_extention = split_filename[0]
    return "%s-%s.%s" % (re.sub('[^A-Za-z0-9]+', '', clase), slugify(filename_without_extention), file_extention)
