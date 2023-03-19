x = 1236477182
print(type(x))
list=list(str(x))
print(list)
a = tuple(list)
print(a)
print(type(a))

z = str(x)
x = z.split(',')
print(x)
