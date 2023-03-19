stroka = 'а роза упала на лапу азора'
stroka1 = 'time to up'
list = list(stroka)
list1 = []
x = len(list)
for i in range(x):
    list1.append(list[x-len(list)-1])
    x = x-1
print(list)
print(list1)

for i in list:
    if i == ' ':
        a=list.index(i)
        list.pop(a)

for i in list1:
    if i == ' ':
        a=list1.index(i)
        list1.pop(a)


s=''.join(list)
s1=''.join(list1)

print(s)
print(s1)

if list==list1:
    print('this is palindrome')
else:
    print('this is not palindrome')