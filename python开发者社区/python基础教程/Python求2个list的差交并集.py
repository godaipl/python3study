listA = [1, 2, 4, 5]

listB = [2, 4, 6, 7, 8]

# 差集
print(list(set(listA) ^ set(listB)))

# B中没有的A集合
print(list(set(listA).difference(set(listB))))

# 并
print(list(set(listA).union(set(listB))))

# 交
print(list(set(listA).intersection(set(listB))))
