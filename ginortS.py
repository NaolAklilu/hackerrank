string = input()
lower_case = []
upper_case = []
digit = []

for i in string:
    if i.islower() == True:
        lower_case.append(i)
    elif i.isupper() == True:
        upper_case.append(i)
    elif i.isdigit() == True:
        digit.append(i)

lower_case = ''.join(sorted(lower_case))
upper_case = ''.join(sorted(upper_case))
odd_digit = []
even_digit = []
for num in digit:
    if int(num) % 2 == 0:
        even_digit.append(num)
    elif int(num) % 2 != 0:
        odd_digit.append(num)

even_digit = ''.join(sorted(even_digit))
odd_digit = ''.join(sorted(odd_digit))

print(lower_case + upper_case + odd_digit + even_digit)
