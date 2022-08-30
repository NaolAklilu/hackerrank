if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # print(query_name)
    for student in student_marks:
        total = 0
        if student == query_name:
            for mark in student_marks[student]:
                total += mark
            average = total / 3.00
            print(format(average,".2f"))
