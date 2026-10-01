#  Student Grades
# Suggested time: 20–25 minutes
# Problem
# Given a list of dictionaries representing students and their scores, calculate each student's average and assign a letter grade. 
# Examples
# students = [{"name": "Sam", "scores": [80, 90]}, {"name": "David", "scores": [55, 60]}]
# Sam → Average: 85.00 → Grade: A
# David → Average: 57.50 → Grade: C 
# Grading System
# 70–100 → A
# 60–69  → B
# 50–59  → C
# 45–49  → D
# 40–44  → E

students = [{"name": "Sam", "scores": [80, 90]},
             {"name": "David", "scores": [55, 60]}]

for x in range(len(students)):
    sum = 0
    for item in students[x]["scores"]:
        sum += item
    avg = sum / len(students[x]["scores"])

    if avg >= 70:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    elif avg >= 45:
        grade = "D"
    elif avg >= 40:
        grade = "E"
    else:
        grade = "fail"

    print(f"Name: {students[x]["name"]}   Average: {avg}   Grade: {grade}")

