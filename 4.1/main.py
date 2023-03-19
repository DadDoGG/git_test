
f = open('unsorted_names.txt')
spis = sorted(list(f.readlines()))
my_file = open("sorted_names.txt", "w+")
for i in range(len(spis)):
    my_file.write(spis[i])
f.close()
my_file.close()