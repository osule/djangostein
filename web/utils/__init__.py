import os

import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'web.settings'
django.setup()


def add(*args):
    return sum(args)