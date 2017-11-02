#
# Setting up the DB
#

import sqlite3

dbfile = 'crawl.db'

conn = sqlite3.connect(dbfile)
cur = conn.cursor()

#
# url: the web address
# visit: 0 (not visited) or 1 (visited)

cur.execute('''CREATE TABLE IF NOT EXISTS Pages (
        url     TEXT UNIQUE,
        visit   INTEGER
        )''')
