from itertools import groupby

string = input()
result = []
for k, g in groupby(string):
    result.append((len(list(g)), int(k)))
print(*result)
