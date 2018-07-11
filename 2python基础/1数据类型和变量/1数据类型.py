# 数据类型

# 整数 int
a = 1
b = 100
c = -100
d = 0

# 浮点数 float
f_a = 1.0
# 1.23乘以10的9次方
f_b = 1.23e9
print('1.23e9 is ', f_b)

# 字符串 string
str1 = 'a'
str2 = "'a'"
str3 = "I'm OK"
str4 = "I'm \"OK\""
print(str4)

# 使用 r'' 来标注相应内容无需转义
print(r'\t\n')

# 使用以下方式替换\n 换行操作
print('''aaaaaa
bbbbbb
cccccc''')

# 布尔值 boolean
print(True)
print(False)
print(True or False)
print(True and True)
print(not True)

# 空值
print(None)
if None:
    print(1)

if not None:
    print(2)