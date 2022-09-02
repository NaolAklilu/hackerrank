from collections import deque

N = int(input())
d = deque()

for _ in range(0, N):
    entry = input().split()
    if entry[0] == 'append':
        d.append(int(entry[1]))
    elif entry[0] == 'appendleft':
        d.appendleft(int(entry[1]))
    elif entry[0] == 'pop':
        d.pop()
    elif entry[0] == 'popleft':
        d.popleft()

print(*d)
