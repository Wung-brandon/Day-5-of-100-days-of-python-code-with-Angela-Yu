#code to calculate the maximum score in a list of student scores
student_score = input("Enter a list of student height: ").split()
#12 45 78 986 78 41 72 10 

for n in range(0,len(student_score)):
    student_score[n] = int(student_score[n])
print("Student score: ",student_score)
#Student score:  [12, 45, 78, 986, 78, 41, 72, 10]

#print("The highest score is:",max(student_height))

max_score = 0
for score in student_score:
    if score > max_score:
        max_score = score
print("The max score is",max_score)
#The max score is 986
