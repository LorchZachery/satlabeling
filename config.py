import os
from os.path import join, dirname, realpath

class Config(object):
        SECRET_KEY = 'secert-key'
        UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'app/static/uploads/')
        TESTING = True
