if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = []
    for i in arr:
        if i not in scores:
            scores.append(i)
    scores.sort()
    print(scores[-2])
