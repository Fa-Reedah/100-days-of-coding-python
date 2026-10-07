# import random
numbers = [1,1,2,3,5,8,13,34,55]

# squared_numbers = [num ** 2 for num in numbers]
#
# print(squared_numbers)

# result = [num for num in numbers if num % 2 == 0]
#
# print(result)

# with open("file1.txt",) as file1:
#     content1 = file1.readlines()
#
# with open("file2.txt") as file2:
#     content2 = file2.readlines()
#
#
# result = [int(num) for num in content1 if num in content2]

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_scores = {student: random.randint(1,100) for student in names}
# print(student_scores)
#
# passed_scores = {student:score for (student,score) in student_scores.items() if score >= 60}
# print(passed_scores)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# result = {word: len(word ) for word in sentence.split()}
#
#
# print(result)

# weather_c ={
#     "Monday":12,
#     "Tuesday":14,
#     "Wednesday":15,
#     "Thursday":14,
#     "Friday":21,
#     "Saturday":22,
#     "Sunday":24,
# }
#
# weather_f = {day: ((temp_c * 9/5) +32) for (day,temp_c) in weather_c.items()}
# print(weather_f)

import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)