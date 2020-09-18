
class SearchUI:
    '''SearchUI provides a means of easily assembling a search interface
    for either Elasticsearch or LunrJS powered search services'''

    def __init__(self, cfg):
        self.cfg = {}
        for key in cfg.keys():
            self.cfg[key] = cfg.get(key, None)
        if not ('id' in self.cfg):
            self.cfg['id'] = 'id'
        if not ('href' in self.cfg):
            self.cfg['href'] = 'href'
        if not ('display_fields' in self.cfg):
            self.cfg['display_fields'] = []
        if not ('aggregated_fields' in self.cfg):
            self.cfg['aggregated_fields'] = []
        if not ('sort_fields' in self.cfg):
            self.cfg = []

