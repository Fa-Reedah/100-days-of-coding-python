"""Daysin Month Exercise"""


def is_leap(Year):
    """Takes Year and check for leap year"""
    if Year % 4 == 0:
        if Year % 100 == 0:
            if Year % 400 == 0:
                return True   # print("It is a Leap Year!")
        else:
            return True   # print("It is a Leap Year!")
    else:
        return False   # print("It is not a Leap Year!")


def days_in_month(year_, month_):
    """Takes year and month input, checks for leap year and return number of
     days in the month"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_leap_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month_ > 12 or month < 1:
        return "Invalid input"
    if is_leap is True:
        num_days = month_leap_days[month_ - 1]
    else:
        num_days = month_days[month_ - 1]

    return num_days


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)