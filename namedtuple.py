from collections import namedtuple

total_numbers = int(input())
columns = input().split()
Student = namedtuple('Student', [columns[0], columns[1], columns[2], columns[3]])

total_mark = 0
for _ in range(0, total_numbers):
    column_entry = input().split()
    student = Student(column_entry[0], column_entry[1],column_entry[2] , column_entry[3])
    total_mark += int(student.MARKS)
    
print(format(total_mark/total_numbers))
