import os
import hashlib
import base64

ORIGIN_URL_PATH = 'url_store'

class Shorter(object):

    def __init__(self):
        if not os.path.isdir(ORIGIN_URL_PATH):
            os.mkdir(ORIGIN_URL_PATH)

    def validate(self, url):
        tiny_url = hashlib.md5(url).hexdigest().rstrip("=")
        path = "%s/%s" % (ORIGIN_URL_PATH, url)
        return os.path.exists(path), tiny_url
    
    def encode(self, url, ori_url):
        tiny_url = hashlib.md5(url).hexdigest().rstrip("=")
        path = "%s/%s" % (ORIGIN_URL_PATH, tiny_url)
        with open(path, "w") as fd:
            fd.write(ori_url)
        return tiny_url

    def decode(self, tiny_url):
        url = ""
        path = "%s/%s" % (ORIGIN_URL_PATH, tiny_url)
        with open(path) as fd:
            url = fd.read()
        return url 
