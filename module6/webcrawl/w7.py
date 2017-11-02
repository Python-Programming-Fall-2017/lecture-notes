#
# pick an un-visited page from the DB


cur.execute('SELECT url FROM Pages WHERE visit = 0 LIMIT 1')
row = cur.fetchone()
if row is not None:
    print("Starting from existing web crawls.")
    domain_base = urllib.parse.urlparse(row[0]).netloc
else:  # new run
    url, domain_base = get_start_url()
    cur.execute('INSERT OR IGNORE INTO Pages (url,visit) VALUES (?,0)', (url,))
    conn.commit()