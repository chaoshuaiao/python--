import sqlite3

db = sqlite3.connect("F:\python文件\sql\sql_test.db")

#查找
# cur = db.cursor()
# sql = "select * from user"#查找全部的数据
# sql2 = 'select * from user where id = 1500'#where 是查找条件
# sql3 = "select name,age from user"#查找user表中的name和age列  
# sql4 = "select * from user order by id desc"#查找user表中的所有数据，并按id倒序排列,desc表示降序,asc表示升序
# cur.execute(sql)
# result = cur.fetchall()#获取全部的数据
# result2 = cur.fetchone()#获取一条数据
# print(result)

#插入
# cur = db.cursor()
# cur.execute("insert into user values(1500,'张三',25,null,'2021-01-01')")#插入数据    
# mylist = [(1700,"lisi",25,None,"2021-01-01"),
#           (1800,"wangwu",25,None,"2021-01-01"),
#           (1900,"zhaoliu",25,None,"2021-01-01")]
# cur.executemany("insert into user values(?,?,?,?,?)",mylist)#插入多条数据
# db.commit()#提交事务
# result = cur.fetchall()#获取数据
# print(result)


#更新
# cur = db.cursor()
# sql = "update user set name = '李四"#更新所有的列，将name改为'张三'
# sql2 = "update user set name = '张三',age = 25 where id = 1500"#更新id为1500的name和age

# sql3 = "update user set name = ?,age = ? where id = ?"#和sql2一样，只是把sql2中的值替换成问号，然后在后面加上值
# cur.execute(sql3,('李四',26,1500))

# cur.execute(sql2)
# db.commit()#提交事务
# result = cur.fetchall()#获取数据
# print(result)



#删除
# db = sqlite3.connect("F:\python文件\sql\sql_test.db")
# cur = db.cursor()
# sql = "delete from user "#删除全部的数据
# sql2 = "delete from user where id = 1500"#删除id为1500的数据
# cur.execute(sql2)
# db.commit()#提交事务
# result = cur.fetchall()#获取数据
# print(result)

#删除数据表
# cur = db.cursor()
# cur.execute("drop table if exists user")
# db.commit

cur = db.cursor()
cur.close()
db.close()
