
import os
import sys
import json

from .logger import Logger

log = Logger(os.getpid())

class Configuration:
    '''This is a configuration object that validates a JSON configuration and provides access to the site settings'''

    def __init__(self):
        '''initialize our configuration object'''
        self.config = {}
        self.config_name = ''

    def load_config(self, f_name):
        '''this reads a JSON configuration from disc and configures self'''
        self.config = {}
        self.config_name = f_name
        if os.path.exists(f_name):
            data = {}
            with open(f_name) as f:
                src = f.read()
                try:
                    data = json.loads(src)
                except Exception as err:
                    log.print(f'ERROR reading {f_name}, {err}')
                    return False
            for key in data:
                self.config[key] = data[key]
        return True                

    def get(self, key, default = None):
        if key in self.config:
            return self.config[key]
        return default

    def required(self, settings):
        '''This checks if the list of configuration fields provided have been set'''
        f_name = self.config_name
        ok = True
        for setting in settings:
            if not setting in self.config:
                print(f'{setting} not in {f_name}')
                ok = False
        return ok                

    def toJSON(self):
        o = {}
        for key in self.config:
            if self.config[key]:
                o[key] = self.config[key]
        s = json.dumps(o)
        return s
