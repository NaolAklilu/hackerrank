n, m  = map(int, input().split())
array = list(map(int, input().split()))
liked_array = set(map(int, input().split()))
disliked_array = set(map(int, input().split()))

happiness = 0
for num in array:
    if num in liked_array:
        happiness += 1
    elif num in disliked_array:
        happiness -= 1

print(happiness)
