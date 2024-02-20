import pymysql

# 创建一个连接对象，然后用这个连接对象创建一个游标对象
conn = pymysql.connect(host='localhost', user='root', password='123456', database='test')
cursor = conn.cursor()


# 插入一条数据
cursor.execute("INSERT INTO user VALUES (1234, 234, 345, 456)")

# 提交事务
conn.commit()

cursor.close()
conn.close()


