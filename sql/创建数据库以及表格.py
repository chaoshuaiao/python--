import sqlite3

# insert into user values(1,"张三",25,null,"2021-01-01")

db = sqlite3.connect("F:\python文件\sql\sql_test.db")#连接数据库，如果不存在则创建
# cursor = db.cursor()#获取游标,要操作数据库一般要通过光标进行
# sql = "create table if not exists user(id integer primary key,name text,age int,picture blob,date date)"
# cursor.execute(sql)
# cursor.execute("insert into user values(1500,'张三',25,null,'2021-01-01')")#插入数据    
# mylist = [(1700,"lisi",25,None,"2021-01-01"),
#           (1800,"wangwu",25,None,"2021-01-01"),
#           (1900,"zhaoliu",25,None,"2021-01-01")]
# cursor.executemany("insert into user values(?,?,?,?,?)",mylist)#插入多条数据
# db.commit()#提交事务
# cursor.fetchone()#获取一条数据
# cursor.fetchall()#获取所有数据
# cursor.close()#关闭游标

# db.close()#关闭数据库
#drop table if exists user#删除学生表，最后别忘了加db.commit()

cur = db.cursor()

sql = "select * from user where id = 1500"
cur.execute(sql)
result = cur.fetchone()
print(result)

cur.close()
db.close()