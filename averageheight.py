
#student_height = [2,3,4,98,47,39,38,74,478]
student_height = input("Enter a list of student height: ").split()
#total_height  = sum(student_height)
#number_of_student = len(student_height)
#average_height = round(total_height / number_of_student)
#print("Average Height:", average_height)

for n in range(0,len(student_height)):
    student_height[n] = int(student_height[n])
print("Student Height: ",student_height)

total_height = 0
for height in student_height:
    total_height += height
print("Total Height:", total_height)

number_of_student = 0
for student in student_height:
    number_of_student += 1
print("Total Number of Students: ",number_of_student)

average_height = round(total_height / number_of_student)
print("Average Height:", average_height)
