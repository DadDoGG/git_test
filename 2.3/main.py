str = "welcome to the jungle"
list = list(str)
list2 = []
x = 0
z = 0
b = -1
for i in str:
    x = x+1
    if i == ' ':
        list2.append(str[z:x])
        z = x
list2.append(str[z:x])

print(list2)