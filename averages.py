
#this is just comment

participation_weight = 0.15
test_weight = 0.45
project_weight = 0.40
print("Enter student's participation grade.")
participation_grade = float(input())

print("Enter student's first test grade.")
test_grade1 = float(input())

print("Enter student's second test grade.")
test_grade2 = float(input())

print("Enter student's third test grade.")
test_grade3 = float(input())

test_average = (test_grade1+test_grade2+test_grade3)/3

print(f"Test average: {test_average:.2f}")

print("Enter student's first project grade.")
project_grade1 = float(input())

print("Enter student's second project grade.")
project_grade2 = float(input())

project_average_grade = (project_grade1 + project_grade2)/2
#this is another comment
print(f"Project average: {project_average_grade:.2f}")

student_grade = participation_grade*participation_weight + test_average * test_weight + project_weight*project_average_grade
print(f"Student grate:  {student_grade:.2f}")