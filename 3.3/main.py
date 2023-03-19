import collections
col = collections.Counter()
def add(x):
    for letter in x:
        col[letter] += 1
    return col
print(add('AZZZBUKA'))