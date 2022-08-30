if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(0,N):
        entry = input().split()
        if entry[0] == "insert":
            arr.insert(int(entry[1]), int(entry[2]))
        elif entry[0] == "remove":
            arr.remove(int(entry[1]))
        elif entry[0] == "append":
            arr.append(int(entry[1]))
        elif entry[0] == "sort":
            arr.sort()
        elif entry[0] == "pop":
            arr.pop()
        elif entry[0] == "reverse":
            arr.reverse()
        elif entry[0] == "print":
            print(arr)
