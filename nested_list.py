if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = []
        student.append(name)
        student.append(score)
        students.append(student)
        
    scores = []
    for student in students:    
        for i in student:
            if student[1] not in scores:
                scores.append(student[1])
                
    scores.sort()
    
    selected_students = []
    for student in students:
        if scores[1] in student:
            selected_students.append(student[0])
    selected_students.sort()
    for name in selected_students:
        print(name)
