line = list(map(int, input().split()))

total = 0
subject_mark = []
for _ in range(0 , line[1]):
    entry = list(map(float,input().split()))
    subject_mark.append(entry)

zipped_mark = list(zip(*subject_mark))
for subject in zipped_mark:
    average = sum(subject)/line[1]
    print(average)
