import re

if __name__ == '__main__':
    for _ in range(0, int(input())):
        regex = input()
        try:
            re.compile(regex)
            print(True)
        except:
            print(False)
