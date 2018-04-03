from org.apache.nifi.lookup import LookupService
from java.util import Optional
import requests
import urllib


class HTTPLookupService(LookupService):

    def __init__(self, endpoint, required_keys=None):
        self.required_keys = required_keys or []
        self.endpoint = endpoint

    def initialize(self, context):
        pass

    def lookup(self, coordinates):
        qs = urllib.urlencode(coordinates)
        r = requests.get('%s?%s' % (self.endpoint, qs))
        if r.status_code == 200:
            j = r.json()
            return Optional.ofNullable(j['value'])
        raise Exception('Fail!')

    def getPropertyDescriptors(self):
        pass

    def getRequiredKeys(self):
        return set(self.required_keys)
