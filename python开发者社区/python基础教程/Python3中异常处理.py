'''
常见异常：
Exception                        所有异常的基类
AttributeError                 特性应用或赋值失败时引发
IOError                             试图打开不存在的文件时引发
IndexError                       在使用序列中不存在的索引时引发
KeyError                          在使用映射不存在的键时引发
NameError                       在找不到名字（变量）时引发
SyntaxError                     在代码为错误形式时引发
TypeError                         在内建操作或者函数应用于错误类型的对象是引发
ValueError                       在内建操作或者函数应用于正确类型的对象，但是该对象使用不合适的值时引发
ZeroDivisionError          在除法或者摸除操作的第二个参数为0时引发
'''

'''python2
try:
    raise Exception("1111")
except Exception, e:
    print(e)
'''

'''python3'''
try:
    raise Exception("1111")
except Exception as e:
    print(e)
