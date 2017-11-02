# 
import urllib.request

url = 'http://www.ucla.edu'

doc = urllib.request.urlopen(url)
html = doc.read().decode()

urls = ['http://www.ucla.edu', 
        'https://archive.org/download/' + 
            'testmp3testfile/mpthreetest.mp3']

p1 = urllib.request.urlopen(urls[0])
h1 = p1.info()  # meta information about the
h1.items()      # header info

p2 = urllib.request.urlopen(urls[1])
h2 = p2.info()
#print(h2)
h2.get_content_type()