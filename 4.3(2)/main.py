import csv
file = open("students.csv")
my_file = open("sorted_age.csv", "w+", newline='\n')
listok = list(file)
listok.pop(0)
print(listok)
listochek = []
for i in listok:
    sperm = i.split(',')
    print(sperm)
    listochek.append(sperm[1])
    listochek = sorted(listochek)

for i in range(len(listochek)):
    for j in listok:
        malyha = min(listochek)
        sperm = j.split(',')
        if sperm[1] == malyha:
            sperm[2] = sperm[2].replace('\n', '')
            my_file.write(str(sperm[0]))
            my_file.write(',')
            my_file.write(str(sperm[1]))
            my_file.write(',')
            my_file.write(str(sperm[2]))
            my_file.write('\n')
            listochek.pop(0)





