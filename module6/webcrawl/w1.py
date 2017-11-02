# urlopen, urlparse

import urllib.request

url = 'http://www.ucla.edu'

doc = urllib.request.urlopen(url)

html = doc.read().decode()

# Parse
r1 = urllib.parse.urlparse('http://www.ucla.edu')
r2 = urllib.parse.urlparse('https://www.google.com/about')
