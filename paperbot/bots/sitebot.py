from ..utils import util, summarizer

class SiteBot:
    """SiteBot for paperbot."""
    def __init__(self, conf='', year=None, root_dir=''):
        
        # define data
        self._conf = conf
        self._year = year
        self._root_dir = root_dir
        
        # acquire settings
        args = util.load_settings(conf)
        self._args = {} if str(year) not in args.keys() else args[str(year)]
        self._tracks = None
        self._baseurl = None
        
        # define container
        self._paperlist  = [] # hold the paperlist during the crawl
        self._summary_all_tracks = {} # hold the summary per track
        self._keyword_all_tracks = {} # hold the keywords per track
        self._paths = {}
        
        # summarizer
        self.summarizer = summarizer.Summarizer() # summarizer called per track
        
    @property
    def paperlist(self):
        return self._paperlist
    
    @property
    def summary_all_tracks(self):
        return self._summary_all_tracks
    
    @property
    def keywords_all_tracks(self):
        return self._keyword_all_tracks
    
    @summary_all_tracks.setter
    def summary_all_tracks(self, summary):
        self._summary_all_tracks = summary
        
    @keywords_all_tracks.setter
    def keywords_all_tracks(self, keywords):
        self._keyword_all_tracks = keywords
        
    @summary_all_tracks.getter
    def summary_all_tracks(self):
        return self._summary_all_tracks
    
    @keywords_all_tracks.getter
    def keywords_all_tracks(self):
        return self._keyword_all_tracks
    
    def __call__(self):
        pass
    
    def ping(self, target=None):
        pass
    
    def crawl(self, target=None):
        pass
    
    def launch(self, fetch_site=False):
        pass
