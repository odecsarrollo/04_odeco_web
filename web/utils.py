import random

import re
from django.utils import timezone


def get_image_name(clase, filename):
    split_filename = filename.split(".")
    file_extention = split_filename[-1]
    return "%s-%s.%s" % (re.sub('[^A-Za-z0-9]+', '', clase), filename, file_extention)
