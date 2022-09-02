line = list(map(int, input().split()))
x = line[0]
k = line[1]
polynomial = input()

if eval(polynomial.replace('x', str(x))) == k:
    print(True)
else:
    print(False)
