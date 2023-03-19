s = 'replace some "this"(\') on \'this\'(\") and vise\' versa\" '
list = list(s)
print(list)
b = []
for i in list:
    if i == '\"':
        c = list.index(i)
        b.append(c)
        list.pop(c)
        list.insert(c, ' ')
for i in list:
    if i == '\'':
        a=list.index(i)
        list.pop(a)
        list.insert(a, '\"')
for i in b:
    list.pop(i)
    list.insert(i, '\'')
stroka = ''.join(list)
print(stroka)