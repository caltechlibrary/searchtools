import os
import json

from lunr import lunr
from lunr.index import Index

from .logger import Logger

log = Logger(os.getpid())

def make_serialized_index(cfg):
    '''make_serialized_index(f_name, i_name) generates a Lunr serialized index as i_name based on a JSON array document f_name.'''
    index_documents = cfg.get('index_documents', '')
    index_id = cfg.get('index_id', 'id')
    index_fields = cfg.get('index_fields', [ 'title' ])
    if index_documents == '':
        log.print(f'index_documents not set in {cfg.config_name}')
        return False
    serialized_index = cfg.get('serialized_index', '')
    if (serialized_index == ''):
        log.print(f'serialized_index not set in {cfg.config_name}')
        return False
    documents = []
    with open(index_documents) as f:
        src = f.read()
        try:
            documents = json.loads(src)
        except Exception as err:
            log.print(f'Invalid {index_documents}, {err}')
            return False
        try:
            idx = lunr(
                ref = index_id, fields = index_fields, documents = documents
            )
            data = idx.serialized()
            src = json.dumps(data)
        except Exception as err:
            log.print('Failed to serialize {serialized_index}, {err}')
            return False
        with open(serialized_index, 'w') as f:
            f.write(src)
    return True



class Query:
    '''This is a class that maps a query string to either Elasticsearch or sserver side Lunr based on the configuration'''
    def __init__(self, cfg):
        self.engine_type = cfg.get('engine', 'lunr')
        if self.engine_type == 'lunr':
            i_name = cfg.get('serialized_index', '')
            if (i_name == ''):
                log.fatal(f'serialized_index not set in {cfg.config_name}')
            if not os.path.exists(i_name):
                log.fatal(f"Can't find {i_name}")
            # Load our serialized LunrJS index                            
            with open(i_name) as f:
                src = f.read()
                try:
                    serialized_index = json.loads(src)
                except Exception as err:
                    log.fatal(f'error loading {i_name}, {err}')
                self.idx = Index.load(serialized_index)
        else:
            log.fatal(f'Unsupported engine_type "{self.engine_type}"')

    def search(self, q):
        results = { 'meta': {'q': q}, 'results': []}
        if self.engine_type == 'lunr':
            results['results'] = self.idx.search(q)
        #elif self.engine_type == 'elasticsearch':
        #    #NOTE: FIXME: do an Elasticsearch query
        else:
            log.print(f'{self.engine_type}, unsupported search engine')
        return results
       
