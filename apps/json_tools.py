import urllib
import json

from apps.url_tools import *


# JSON tools
def generate_json(api_url):
    
    return json.loads(download_website(api_url))
