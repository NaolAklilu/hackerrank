from collections import Counter

N = int(input())
shoes_size = list(map(int, input().split()))
size_and_count = list(Counter(shoes_size).items())

size_count = []
for i in size_and_count:
    size_count.append(list(i))

earned_money = 0
for i in range(0, int(input())):
    entry = input().split()
    for shoe_size in size_count:
        if int(entry[0]) == shoe_size[0] and shoe_size[1] > 0:
            earned_money += int(entry[1])
            shoe_size[1] -= 1
            
print(earned_money)
