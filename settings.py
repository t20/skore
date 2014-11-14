import json
import os

class Config(object):
    """Default config"""
    DEBUG = True
    APP_SECRET_KEY = '-7\x87\xf3\x8e\xee\xcc\xb4\x1a\x12_\xdd\xe4O\x01\x84\xaa\x94\xed8\xbe\x92\xc5\xf8'

    REDIS_DB = 0
    REDIS_PORT = 6379
    REDIS_HOST = 'localhost'
