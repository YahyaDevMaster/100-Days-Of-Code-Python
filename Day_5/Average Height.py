# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
numofstudent = 0
totalsum = 0
for student in student_heights:
    totalsum += student
    numofstudent += 1
print(f"total height = {totalsum}")
print(f"number of students = {numofstudent}")
print(f"average height = {round(totalsum/numofstudent)}")

# Write your code below this row 👇
