
import os
import sys
import json

from .logger import Logger

log = Logger(os.getpid())

class Configuration:
    '''This is a configuration object that validates a JSON configuration and provides access to the site settings'''

    def __init__(self):
        '''initialize our configuration object'''
        self.htdocs = 'htdocs'
        self.static = 'static'
        self.templates = 'templates'
        self.organization = ''
        self.site_title = ''
        self.site_welcome = ''
        self.bucket = ''
        self.distribution_id = ''
        self.config_name = ''
        self.base_url = ''
        self.base_path = ''
        self.dataset = ''
        self.elastic_documents_max_no = 25
        self.elastic_documents = ''
        self.elastic_base_endpoint = ''
        self.elastic_api_key = ''
        self.elastic_engine_name = ''
        self.custom = {}

    def load_config(self, f_name):
        '''this reads a JSON configuration from disc and configures self'''
        self.config_name = f_name
        if os.path.exists(f_name):
            with open(f_name) as f:
                src = f.read()
                try:
                    data = json.loads(src)
                except Exception as err:
                    log.print(f'ERROR reading {f_name}, {err}')
                    return False
                ok = True
                for key in data:
                    if 'elastic_documents_max_no' == key:
                        self.elastic_documents_max_no = data[key]:
                    elif 'elastic_documents' == key:
                        self.elastic_documents = data[key]
                    elif 'elastic_base_endpoint' == key:
                        self.elastic_base_endpoint = data[key]
                    elif 'elastic_api_key' == key:
                        self.elastic_api_key = data[key]
                    elif 'elastic_engine_name' == key:
                        self.elastic_engine_name = data[key]
                    elif 'base_path' == key:
                        self.base_path = data[key]
                    elif 'base_url' == key:
                        self.base_url = data[key]
                    elif 'htdocs' == key:
                        self.htdocs = data[key]
                        if not os.path.exists(self.htdocs):
                            log.print(f'ERROR: htdocs setting, "{self.htdocs}" from {f_name} does not exist.')
                            ok = False
                    elif 'static' == key:
                        self.static = data[key]
                        if not os.path.exists(self.static):
                            log.print(f'ERROR: htdocs setting, "{self.static}" from {f_name} does not exist.')
                            ok = False
                    elif 'templates' == key:
                        self.templates = data[key]
                        if not os.path.exists(self.templates):
                            log.print(f'ERROR: htdocs setting, "{self.templates}" from {f_name} does not exist.')
                            ok = False
                    elif 'dataset' == key:
                        self.dataset = data[key]
                        if not os.path.exists(self.dataset):
                            log.print(f'ERROR: dataset collection "{self.dataset}" does not exist.')
                            ok = False
                    elif 'organization' == key:
                        self.organization = data[key]
                    elif 'site_welcome' == key:
                        self.site_welcome = data[key]
                    elif 'site_title' == key:
                        self.site_title = data[key]
                    elif 'bucket' == key:
                        self.bucket = data[key]
                    elif 'distribution_id' == key:
                        self.distribution_id = data[key]
                    else:
                        self.custom[key] = data[key]
        else:
            ok = False
        return ok                

    def get(self, key, default = None):
        if key in self.custom:
            return self.custom[key]
        ok = True
        value = None
        if ('elastic_documents_max_no' == key):
            value = self.elastic_documents_max_no
            if (self.elastic_documents_max_no == 0):
                ok = False
        if ('elastic_documents' == key):
            value = self.elastic_documents
            if (self.elastic_documents == ''):
                ok = False
        if ('elastic_base_endpoint' == key):
            value = self.elastic_base_endpoint
            if (self.elastic_base_endpoint == ''):
                ok = False
        if ('elastic_api_key' == key):
            value = self.elastic_api_key
            if (self.elastic_api_key == ''):
                ok = False
        if ('elastic_engine_name' == key):
            value = self.elastic_engine_name
            if (self.elastic_engine_name == ''):
                ok = False
        if ('base_path' == key):
            value = self.base_path
            if (self.base_path == ''):
                ok = False
        if ('base_url' == key):
            value = self.base_url
            if (self.base_url == ''):
                ok = False
        if ('htdocs' == key):
            value = self.htdocs
            if (self.htdocs == ''):
                ok = False
            elif not os.path.exists(self.htdocs):
                ok = False
        if ('static' == key):
            value = self.static
            if (self.static == ''):
                ok = False
            elif not os.path.exists(self.static):
                ok = False
        if ('templates' == key):
            value = self.templates
            if (self.templates == ''):
                ok = False
            elif not os.path.exists(self.templates):
                ok = False
        if ('dataset' == key):
            value = self.dataset
            if (self.dataset == ''):
                ok = False
            elif not os.path.exists(self.dataset):
                ok = False
        if ('organization' == key) and (self.organization == ''):
            value = self.organization
            ok = False
        if ('site_welcome' == key) and (self.site_welcome == ''):
            value = site_welcome
            ok = False
        if ('site_title' == key) and (self.site_title == ''):
            value = site_title
            ok = False
        if ('bucket' == key) and (self.bucket == ''):
            value = self.bucket
            ok = False
        if ('distribution_id' == key) and (self.distribution_id == ''):
            value = self.distribution_id
            ok = False
        if ok:
            return value
        return default

    def required(self, settings):
        '''This checks if the list of configuration fields provided have been set'''
        f_name = self.config_name
        ok = True
        for setting in settings:
            if ('elastic_documents_max_no' in settings):
                if (self.elastic_documents_max_no == 0):
                    print(f'elastic_documents_max_no not set in {f_name}')
                    ok = False
            if ('elastic_documents' in settings):
                if (self.elastic_documents == ''):
                    print(f'elastic_documents not set in {f_name}')
                    ok = False
            if ('elastic_base_endpoint' in settings):
                if (self.elastic_base_endpoint == ''):
                    print(f'elastic_base_endpoint not set in {f_name}')
                    ok = False
            if ('elastic_api_key' in settings):
                if (self.elastic_api_key == ''):
                    print(f'elastic_api_key not set in {f_name}')
                    ok = False
            if ('elastic_engine_name' in settings):
                if (self.elastic_engine_name == ''):
                    print(f'elastic_engine_name not set in {f_name}')
                    ok = False
            if ('base_path' in settings):
                if (self.base_path == ''):
                    print(f'base_path not set in {f_name}')
                    ok = False
            if ('base_url' in settings):
                if (self.base_url == ''):
                    print(f'base_url not set in {f_name}')
                    ok = False
            if ('htdocs' in settings):
                if (self.htdocs == ''):
                    print(f'htdocs not set in {f_name}')
                    ok = False
                elif not os.path.exists(self.htdocs):
                    print(f'htdocs {self.htdocs} does not exist.')
                    ok = False
            if ('static' in settings):
                if (self.static == ''):
                    print(f'static not set in {f_name}')
                    ok = False
                elif not os.path.exists(self.static):
                    print(f'static {self.static} does not exist.')
                    ok = False
            if ('templates' in settings):
                if (self.templates == ''):
                    print(f'templates not set in {f_name}')
                    ok = False
                elif not os.path.exists(self.templates):
                    print(f'templates {self.templates} does not exist.')
                    ok = False
            if ('dataset' in settings):
                if (self.dataset == ''):
                    print(f'dataset not set in {f_name}')
                    ok = False
                elif not os.path.exists(self.dataset):
                    print(f'dataset {self.dataset} does not exist.')
                    ok = False
            if ('organization' in settings) and (self.organization == ''):
                print(f'organization not set in {f_name}')
                ok = False
            if ('site_welcome' in settings) and (self.site_welcome == ''):
                print(f'site_welcome not set in {f_name}')
                ok = False
            if ('site_title' in settings) and (self.site_title == ''):
                print(f'site_title not set in {f_name}')
                ok = False
            if ('bucket' in settings) and (self.bucket == ''):
                print(f'bucket not set in {f_name}')
                ok = False
            if ('distribution_id' in settings) and (self.distribution_id == ''):
                print(f'distribution_id not set in {f_name}')
                ok = False
        return ok                

    def toJSON(self):
        o = {}
        if self.elastic_documents_max_no > 0:
            o['elastic_documents_max_no'] = self.elastic_documents_max_no
        if self.elastic_documents != '':
            o['elastic_documents'] = self.elastic_documents
        if self.elastic_base_endpoint != '':
            o['elastic_base_endpoint'] = self.elastic_base_endpoint
            o['elastic_api_key'] = self.elastic_api_key
        if self.base_path != '':
            o['base_path'] = self.base_path
        if self.base_url != '':
            o['base_url'] = self.base_url
        if self.htdocs != '':
            o['htdocs'] = self.htdocs
        if self.static != '':
            o['static'] = self.static
        if self.templates != '':
            o['templates'] = self.templates
        if self.dataset != '':
            o['dataset'] = self.dataset
        if self.organization != '':
            o['organization'] = self.organization
        if self.site_welcome != '':
            o['site_welcome'] = self.site_welcome
        if self.site_title != '':
            o['site_title'] = self.site_title
        if self.bucket != '':
            o['bucket'] = self.bucket
        if self.distribution_id != '':
            o['distribution_id'] = self.distribution_id
        for key in self.custom:
            o[key] = self.custom[key]
        s = json.dumps(o)
        return s
