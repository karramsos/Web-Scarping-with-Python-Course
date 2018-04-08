import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='mysql')
cur = conn.cursor()
cur.execute("USE scrapingtest")
cur.execute("SELECT * FROM pages where id=1")
print(cur.fetchone())
cur.close()
conn.close()