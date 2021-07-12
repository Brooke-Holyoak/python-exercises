# Conditional Basics
# 1. prompt user for a day of the week, print out whether the day is Monday or no

what_day_of_the_week = input("What day of the week is it?")

if what_day_of_the_week.lower() == "monday":
    print ("Yep, it's a Monday.")
else:
    print ("At least it's not Monday!")

# 1.b prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day_of_the_week = input("What day of the week is it?")

if day_of_the_week.lower() == ("saturday" or "sunday"):
    print ("Yay! It's the weekend!")
else:
    print ("It's a weekday.")

# 1 c. create variables and make up values for

# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

weekly_hours_worked = 45
hourly_rate = 150
over_40_hours_rate = hourly_rate * 1.5
if weekly_hours_worked <= 40:
    print (weekly_hours_worked * hourly_rate)
elif weekly_hours_worked > 40:
    print ((40 * hourly_rate) + ((40 - weekly_hours_worked) * over_40_hours_rate))

i = 5
while i <= 15:
    print(i)
    i += 1

i = 0
while i <= 100:
    print (i)
    i += 2

i = 100
while i >= -10:
    print (i)
    i -= 5

i = 2
while i < 1000000:
    print (i)
    i = i ** 2

i = 100
while i >= 5:
    print (i)
    i -= 5

# Multiplication table (from 1 to 10) in Python

chosen_number = int(input("Enter any number here: "))

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(chosen_number, 'x', i, '=', chosen_number * i)

for r in range(1, 10):
    print(str(r) * r)

