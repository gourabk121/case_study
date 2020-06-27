import os


class Config(object):
    SECRET_KEY= os.environ.get('SECRET_KEY') or "gsdhkisdjoidshsakjL"
    # MONGODB_SETTINGS={'db' : 'hos'}