from collections import Counter
def most_common_words(filepath, number_of_words=3):
    file = open(filepath)
    listok = list(file)
    print(listok)
    stroka = str(listok)
    print(stroka)
    stroka = stroka.replace(',', '')
    stroka = stroka.replace('.', '')
    stroka = stroka.replace('\\n', '')
    listok = stroka.split()
    print(listok)
    cnt = Counter(listok)
    cnt.pop("''")
    print(cnt)
    cnt = dict(cnt)
    for k in list(cnt):
        if cnt[k] < number_of_words:
            cnt.pop(k)
    print(cnt)
print(most_common_words('lorem_ipsum.txt'))



