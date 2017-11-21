import os


class Config(object):
    RAS_SECURE_MESSAGE_DB_URI = os.getenv('RAS_SECURE_MESSAGE_DB_URI', 'postgres://postgres:postgres@localhost:6432/postgres')
