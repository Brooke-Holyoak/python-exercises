# Conditional Basics
# 1. prompt user for a day of the week, print out whether the day is Monday or no

what_day_of_the_week = input("What day of the week is it?")

if what_day_of_the_week == "Monday":
    print ("Yep, it's a Monday.")
else:
    print ("At least it's not Monday!")

# 1.b prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day_of_the_week = input("What day of the week is it?")

if day_of_the_week.lower() == ("saturday" or "sunday"):
    print ("Yay! It's the weekend!")
else:
    print ("It's a weekday.")

