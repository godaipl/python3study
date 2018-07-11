# 1 pymysql
import pymysql

# 创建连接
conn = pymysql.connect(host='192.168.5.241', port=3306, user='root', passwd='dashu0701', db='loandb')

cursor = conn.cursor()

effect_rows = cursor.execute("update t_collection_case set isClose = 1 WHERE id = 57")

print(effect_rows)

cursor.execute("select * from t_collection_case limit 10")

row1 = cursor.fetchone()

print(row1)

print(row1[0])
print(row1[11])
print(row1[14])

row2_4 = cursor.fetchmany(3)

print(row2_4)

rowAll = cursor.fetchall()

print(rowAll)

# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()