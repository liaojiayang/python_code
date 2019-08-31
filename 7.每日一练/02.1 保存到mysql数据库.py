# 数据库需要用相应的模块读取

import pymssql # 导入pymssql 模块，SQL Server
#import pymysql # 导入pymysql 模块，MySQL

# 数据库连接配置
config = {
          'host':'localhost',
    # 本地数据库，可不输入port/user/password
          #'port':3306,
          #'user':'root',
          #'password':'root',
          'database':'Deyou',
          'charset':'GBK'
          }

# 打开数据库连接
conn = pymssql.connect(**config)
#conn2 = pymysql.connect(**config)

try:
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    # SQL 语句
    read_sql = "SELECT * FROM [dbo].[店东ucid]"
    insert_sql = ""
    update_sql = ""
    delete_sql = ""

    # 执行SQL语句
    cursor.execute(read_sql)
    # 获取结果列表
    results = cursor.fetchall()
    print(results)
    # 确认修改
    conn.commit()

    # 关闭游标
    cursor.close()

    # 关闭链接
    conn.close()
    print("执行成功")
except:
    print("执行失败")
