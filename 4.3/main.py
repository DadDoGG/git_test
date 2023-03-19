def get_top_performers(file_path, number_of_top_students=5):
    file = open(file_path)
    listok = list(file)
    listok.pop(0)
    dictant = {}
    for i in listok:
        for v in i:
            sperm = i.split(',')
            sperm[2] = sperm[2].replace('\n', '')
            sperm.pop(1)
            dictant[sperm[0]] = float(sperm[1])
    print(dictant)

    umnichki = []
    for j in range(number_of_top_students):
        for k,v in dictant.items():
            luchi = max(dictant.values())
        for i in list(dictant):
                if dictant[i] == luchi:
                    if (len(umnichki)) < 5:
                        umnichki.insert(j-1, i)
                        dictant.pop(i)
    return print(sorted(umnichki))


get_top_performers("students.csv")
