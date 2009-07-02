import urllib
from urllib2 import Request, urlopen, URLError, HTTPError

class Justlogging:
  
  api_key = None
  log_key = None
  
  def __init__(self, api_key, log_key):
    self.api_key = api_key
    self.log_key = log_key
  
  def log(self, entry, log_key=None):
    if log_key == None:
      log_key = self.log_key
      
    params = urllib.urlencode({'access_key': self.api_key, 'log_key': log_key, 'entry': entry})
    req = Request("http://logs.justlogging.com/log", params)
    
    try:
      response = urlopen(req)
    except HTTPError, e:
      if e.code == 201:
        return True
      else:
        return False
    else:
       return True