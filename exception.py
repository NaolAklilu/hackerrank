if __name__ == '__main__':
    for _ in range(0, int(input())):
        line = input().split()
        try:
            print(int(line[0])//int(line[1]))
        except ZeroDivisionError as e:
            print ("Error Code:", e)
        except ValueError as exception:
            print ("Error Code:", exception)
