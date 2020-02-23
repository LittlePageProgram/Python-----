addr = ['shanghai', 'beijing', 'chengdu', 'guangzhou', 'xian']

# sort 永远
addr.sort()

# sorted 临时
print(sorted(addr))

addr.reverse()

print(addr)

addr.pop()

addr.pop()

addr.insert(0, '111')

print(addr)

print(addr[-2])
