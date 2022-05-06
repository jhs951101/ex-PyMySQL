import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='(비밀번호)',
                       db='mysql', charset='utf8')
 
curs = conn.cursor(pymysql.cursors.DictCursor)
 
sql = "SELECT User, Host FROM user"
curs.execute(sql) 
rows = curs.fetchall()

for row in rows:
    # print(row)
    # 출력 : {'user': (value1), 'host': (value2)}
    print('user: ', row['User'], ', host: ', row['Host'])

conn.close()
