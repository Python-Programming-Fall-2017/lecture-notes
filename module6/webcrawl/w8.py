#
# Some web site blocks you if you do not use a "normal" user agent
#


import urllib.request
import random
import time

def get_user_agent():
    """
      Return a random user agent from the list
    """
    db = [ 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3 GTB5',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; ko; rv:1.9.1b2) Gecko/20081201 Firefox/3.1b2',
            'Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.9b5) Gecko/2008032620 Firefox/3.0b5',
            'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.12) Gecko/20080214 Firefox/2.0.0.12',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; cs; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8',
            'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.8.0.5) Gecko/20060819 Firefox/1.5.0.5',
            'Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3',
            'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.7.9) Gecko/20050711 Firefox/1.0.5'
        ]
    idx = random.randrange(0, len(db))
    return db[idx]

if __name__ == '__main__':

    url = 'http://www.ucla.edu'

    #req1 = urllib.request.Request(url)  # not specifying user agent
    #r = urllib.request.urlopen(req2)
    #r.read()

    count = 0
    while count < 5:
        agent = get_user_agent()
        print("Agent:{}".format(agent))
        req2 = urllib.request.Request(url, headers = {'User-Agent': agent})
        r = urllib.request.urlopen(req2)
        x = r.read()
        #print(x)
        time.sleep(2)  # sleep 2 second
        count += 1
