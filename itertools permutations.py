from itertools import permutations

line = input().split(" ")
string = ''.join(sorted(line[0]))
string_list = list(permutations(string, int(line[1])))

for char in string_list:
    print(*char,sep='')
