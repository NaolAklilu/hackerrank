from collections import defaultdict

if __name__ == '__main__':
    d = defaultdict(list)
    entry = input().split()
    n = int(entry[0])
    m = int(entry[1])
        
    group_A, group_B = [], []
    
    for _ in range(0, n):
        group_A.append(str(input()))
    group_A.insert(0, 0)
    for _ in range(0, m):
        group_B.append(str(input()))
        
    for b in group_B:
        if b not in group_A:
            d[b].append(-1)
        elif len(d[b]) > 0:
            pass
        else:
            for i in range(1, len(group_A)):
                if group_A[i] == b:
                    d[b].append(i)
             
    for element in group_B:
        print(*d[element])
