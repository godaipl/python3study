# pip3 install sqlalchemy

# create table test
# (
#	id int null,
#	name varchar(20) null
# );

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class Test(Base):
    # 表的名字:
    __tablename__ = 'test'
    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine("mysql+pymysql://root:dashu0701@192.168.5.241:3306/loandb?charset=utf8", max_overflow=5)

DBSession = sessionmaker(bind=engine)

session = DBSession()

# 添加一条数据
new_test = Test(id="1", name="test1")
new_test2 = Test(id="2", name="test2")
new_test3 = Test(id="3", name="test3")

query_test = session.query(Test).filter(Test.id == '1').first()

query_test2 = session.query(Test).filter(Test.id == '2').first()

query_test3 = session.query(Test).filter(Test.id == '2').first()

if (query_test and query_test.id > 0):
    print('new_test is exist')
else:
    session.add(new_test)

if (query_test2 and query_test2.id > 0):
    print('new_test2 is exist')
else:
    session.add(new_test)

if (query_test3 and query_test3.id > 0):
    print('new_test3 is exist')
else:
    session.add(new_test3)

# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
