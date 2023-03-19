list = [1, 2, 3, 8, 9]
la = []
lf = []
x = 0
for i in list:
    la.append(list[x])
    x = x+1
    if len(la) % 2 == 0:
        a = tuple(la)
        lf.append(a)
        la.clear()
        la.append(list[x-1])
print(lf)