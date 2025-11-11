# ================== Question 1 ==================

"""
    Instructions
    In a five-star restaurant review system (⭐️⭐️⭐️⭐️⭐️), the stars typically represent the different levels of satisfaction.

    But what does each of the stars mean?

    Start by creating a rating variable and set it equal to a decimal number.

    Make a rating system using an if/elif/else statement:

    rating greater than 4.5, print 'Extraordinary'
    rating greater than 4, print 'Excellent'
    rating greater than 3, print 'Good'
    rating greater than 2, print 'Fair'
    Everything else, print 'Poor'
"""

rating = 4.3

if rating > 4.5:
  print("Extraordinary")
elif rating > 4:
  print("Excellent")
elif rating > 3:
  print("Good")
elif rating > 2:
  print("Fair")
else:
  print("Poor")

# ================== Question 2 ==================

"""
    Instructions
    U.S. high schools typically last for four years, from freshman year to senior year. 🚌💨

    First, ask the user to enter their grade as an integer.

    Create a four-year high school grade system using an if/elif/else statement:

    grade is 9, print 'Freshman'
    grade is 10, print 'Sophomore'
    grade is 11, print 'Junior'
    grade is 12, print 'Senior'
    Everything else is 'TBD'
"""

grade = int(input("Enter  your grade (as a number): "))

if grade == 9:
  print("Freshman")
elif grade == 10:
  print ("Sophomore")
elif grade == 11:
  print("Junior")
elif grade == 12:
  print("Senior")
else:
  print("TBD")

# ================== Question 3 ==================


"""
    Instructions
    Snapple is a famous tea drink brand from Queens, New York. Each bottle cap comes with a silly fun fact.

    Use the random module to create a number from 0 to 5.

    Then use an if/elif/else statement to print out one of these six random Snapple facts:

    0 - 'Flamingos turn pink from eating shrimp.'
    1 - 'The only food that doesn\'t spoil is honey.'
    2 - 'Shrimp can only swim backwards.'
    3 - 'A taste bud\'s life span is about 10 days.'
    4 - 'It is impossible to sneeze while sleeping.'
    5 - 'It is illegal to sing off-key in North Carolina.'
"""

import random

fact_number = random.randint(0, 5)

if fact_number == 0:
  print("Flamingos turn pink from eating shrimp.")
elif fact_number == 1:
  print("The only food that doesn\'t spoil is honey.")
elif fact_number == 2:
  print("Shrimp can only swim backwards.")
elif fact_number == 3:
  print("A taste bud\'s life span is about 10 days.")
elif fact_number == 4:
  print("It is impossible to sneeze while sleeping.")
else:
  print("It is illegal to sing off-key in North Carolina.")

# ================== Question 4 ==================

"""
    Instructions
    Ah, the four seasons in the year — winter, spring, summer, or fall; all you have to do is call!

    Ask the user the month number using the input() function.

    Check for the four seasons using an if/elif/else statement and logical operators:

    month is 1, 2, 3, print 'Winter 🌨️'
    month is 4, 5, 6, print 'Spring 🌱'
    month is 7, 8, 9, print 'Summer 🌞'
    month is 10, 11, 12, print 'Autumn 🍂'
    Everything else is 'Invalid'
    Logical operators in Python include the and and or keywords. Which one should you use?
"""

month = int(input("Enter the month number (1-12): "))

if month == 1 or month == 2 or month == 3:
    print("Winter 🌨️")
elif month == 4 or month == 5 or month == 6:
    print("Spring 🌱")
elif month == 7 or month == 8 or month == 9:
    print("Summer 🌞")
elif month == 10 or month == 11 or month == 12:
    print("Autumn 🍂")
else:
    print("Invalid")

# ================== Question 5 ==================

"""
    Instructions
    The year is 2199... we have become an interplanetary species and can travel to other planets in the solar system! 🚀

    Create a weight conversion program that:

    Asks the user what their Earth weight is (as a float).
    Asks the user for a planet number (as an int).
    Then, use an if/elif/else statement to calculate the user's weight on the destination planet.

    To calculate the user's weight:

    destination weight=Earth weight × relative gravity
    Number	Planet	Relative Gravity
    1	Mercury	0.38
    2	Venus	0.91
    3	Mars	0.38
    4	Jupiter	2.53
    5	Saturn	1.07
    6	Uranus	0.89
    7	Neptune	1.14
    If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'.
"""

earth_weight = float(input("Enter your weight on Earth (in pounds or kg): "))

planet = int(input("Enter the planet number (1-7): "))

if planet == 1:
  weight = earth_weight * 0.38
  print("Your weight on Mercury is:", weight)
elif planet == 2:
  weight = earth_weight * 0.91
  print("Your weight on Venus is:", weight)
elif planet == 3:
  weight = earth_weight * 0.38
  print("Your weight on Mars is:", weight)
elif planet == 4:
  weight = earth_weight * 2.53
  print("Your weight on Jupiter is:", weight)
elif planet == 5:
  weight = earth_weight * 1.07
  print("Your weight on Saturn is:", weight)
elif planet == 6:
  weight = earth_weight * 0.89
  print("Your weight on Uranus is:", weight)
elif planet == 7:
  weight = earth_weight * 1.14
  print("Your weight on Neptune is:", weight)
else:
  print("Invalid planet number")