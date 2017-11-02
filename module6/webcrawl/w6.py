#
# initial URL
#

import sys

url = input('Enter the domain to crawl (including "http..."): ')
domain_base = urllib.parse.urlparse(url).netloc
print("base domain = ", domain_base)

print('url entered = ', url)
if url.startswith('http'):
    print("url ok")
else:
    print('Must include http in url...')
    sys.exit()
# remove the trailing '/':
if url.endswith('/'):
    url = url[:-1]
    
print(url)