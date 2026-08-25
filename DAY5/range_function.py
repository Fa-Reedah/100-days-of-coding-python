# Range Functions
'''
for number in range(1, 11, 2):
    print(number)


total = 0
for number in range(1, 101):
    total += number
    print(total)
'''

# Exercise
sum_of_even = 0
for even in range(0, 101, 2):
    sum_of_even += even
print(sum_of_even)


# Fizz Buzz

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)
