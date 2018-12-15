import pymysql

conn = pymysql.Connect(host='127.0.0.1', user='root', passwd='Cisco@123', db='test')

cur = conn.cursor()

cur.execute("SELECT user FROM mysql")

print(cur.description)

print()

for row in cur:
   print(row)

cur.close()
conn.close()
