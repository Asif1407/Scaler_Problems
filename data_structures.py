



students = [50, 23, 9, 18, 61, 32]


#using bubble sort
for i in range(len(students)):
    for j in range(0, len(students)- i - 1):
        if students[j] > students[j + 1]:
            students[j], students[j + 1] = students[j + 1], students[j]
print(students)


