# for Loops
'''
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:     # Assigns fruit as a variable to each string in fruits
    print(fruit)
    print(fruit + " pie")
    print(fruits)
print(fruit)
'''

# Exercise

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for h in student_heights:
    total_height += h

num_of_students = 0
for n in student_heights:
    num_of_students += 1

average_height = round(int(total_height / num_of_students))
print(average_height)


# Exercise 2
student_score = input("Input a list of student scores ").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

highest_score = student_score[0]
for s in student_score:
    if s >= highest_score:
        highest_score = s
print(highest_score)


highest_score = student_score[0]
for s in student_score:
    if s <= highest_score:
        highest_score = highest_score
    else:
        highest_score = s
print(highest_score)
