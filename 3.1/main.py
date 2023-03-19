import string
from collections import Counter
alphabet = set(string.ascii_lowercase)
str1 = 'a b c d e'
str2 = 'a f g h i'
str3 = 'a f k l m'
str4 = 'a n o p q r'
str5 = 'a s s g h r'

list1 = set(str1)
list2 = set(str2)
list3 = set(str3)
list4 = set(str4)
list5 = set(str5)

alpha = [list1, list2, list3, list4, list5]
in_two = [str1, str2, str3, str4, str5]

letters = {k for k, v in Counter([l for x in in_two for l in set(x)]).items() if v > 1}
in_all = list1 & list2 & list3 & list4 & list5
in_one = sorted(list1 | list2 | list3 | list4 | list5)
omega = alphabet.difference(list1, list2, list3, list4, list5)



print(in_all)
print(in_one)
print(letters)
print(omega)



