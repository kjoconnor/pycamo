import hashlib
import binascii
from urlparse import urlparse
import requests

CAMO_SHARED_KEY = '9AFJIjnaoijF*JFAHjfmvc'

url = 'https://i2.cdn.turner.com/cnn/dam/assets/120727064412-olympics-begin-7-27-06-video-tease.jpg'

class Camo:

	def unhex_url(self, url):
		return binascii.a2b_hex(url)

	def verify_hash(self, hash, url):
		return hashlib.sha1(CAMO_SHARED_KEY + url).hexdigest() == hash

	def retrieve_url(self, url):
		try:
			content = urllib.urlopen(url)
		except Exception, e:
			print "Exception caught: %s" % e
			return False

		if content.code != 200:
			print "Bad code returned: %s" % content.code
			return False

	def verify_url(self, url):
		parsed_url = urlparse(url)

		scheme = parsed_url[0]

		if scheme != 'http' and scheme != 'https':
			return {'code': '404',
					'resp': 'Unsupported protocol: ' + scheme}

		return True
		

proxy = Camo()
if proxy.verify_url(url):
	proxy.retrieve_url(url)

# print hashlib.sha1(CAMO_SHARED_KEY + url).hexdigest()

# url_hex = binascii.b2a_hex(url)

# print "URLHEX: %s" % url_hex
# print "URLUNHEX: %s" % binascii.a2b_hex(url_hex)