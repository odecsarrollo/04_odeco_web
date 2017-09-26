import random

import re
from django.utils import timezone


def get_image_name(clase, filename):
    split_filename = filename.split(".")
    file_extention = split_filename[-1]

    random_uno = random.randint(1, 9)
    random_dos = random.randint(10, 99)
    random_name = random_uno * random_dos - (random_uno + random_dos)

    fecha_hoy = timezone.now().strftime('%Y%m%d%H%M%S')
    return "%s-%s%s.%s" % (re.sub('[^A-Za-z0-9]+', '', clase), fecha_hoy, random_name, file_extention)
