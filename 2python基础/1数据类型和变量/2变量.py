# 变量名必须是大小写英文、数字和_的组合，且不能用数字开头
# 1_a = 1
a_1 = 1
abc = 2
_abc = 3
_1 = 4
Abc = 5

# a 指向 abc所在内存地址
a = 'ABC'
# b指向 abc所在的内存地址
b = a
# a 指向 xyz所在的内存地址
a = 'XYZ'
print(b)

PI = 3.1415926

print(10 / 3)
print(10 // 3)
print(9 / 3)
print(9 // 3)

print(10 % 3)
