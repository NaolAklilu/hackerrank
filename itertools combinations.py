from itertools import combinations

line = input().split(" ")
string = ''.join(sorted(line[0]))
string_list = []

for i in range(1, int(line[1]) + 1):
    string_list = string_list + list(combinations(string, i))

for char in string_list:
    print(*char,sep='')
