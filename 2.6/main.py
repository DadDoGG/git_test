str = 'Any pythonista like namespaces a lot.'
list = list(str)
list3 = str.split(' ')
list1 = []
z = 0
for i in list:
    z = z+1
    if i == ' ':
        list1.append(z)
        z = 0
z = sum(list1)
z = len(str) - z
list1.append(z)
z = max(list1)
x = list1.index(z)
print(x)
print(z)
print(list1)
print(list3)

print(list3[x])



