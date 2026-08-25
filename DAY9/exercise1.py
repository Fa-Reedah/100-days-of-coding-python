""" EXERCISE """

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for stud in student_scores:
    if student_scores[stud] >= 91:
        student_grades[stud] = "Outstanding"

    elif student_scores[stud] >= 81:
        student_grades[stud] = "Exceeds expectations"

    elif student_scores[stud] >= 71:
        student_grades[stud] = "Acceptable"

    elif student_scores[stud] <= 70:
        student_grades[stud] = "Fail"


print(student_grades)
