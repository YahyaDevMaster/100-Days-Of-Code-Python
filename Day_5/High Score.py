# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
tscore = 0
for hi_score in student_scores:
    if hi_score > tscore:
        tscore = hi_score

print(f"The highest score in the class is: {tscore}")
