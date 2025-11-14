""" ================ Challenge 1 =================="""

"""
    James Bond is a classic movie character that fights bad guys and introduces himself in an iconic way: “Bond, James Bond.”

    Write a greetings() function that takes in two parameters:

    first_name
    last_name
    Print out the phrase with the last name, followed by a comma, and then the full name.

    Next, call the function using your own name, like:

    greetings('Richard', 'Hendricks')

    The output should look like:

    Hendricks, Richard Hendricks

    Note: This function doesn't have a return statement.
"""
def greetings(first_name, last_name):
  print(f"{last_name}, {first_name} {last_name}")

greetings("Dakota", "K")

""" ================ Challenge 2 =================="""

"""
    Finding an average can be a useful way to understand the underlying trends of some data.

    Write an average() function that takes in two parameters:

    num1
    num2
    It should calculate and return the average of the two numbers.

    The average of num1 and num2 is:

    (num1+num2)/2

    Note: Do not use the math module.
"""
def average(num1, num2):
  return (num1 + num2) / 2

print(average(5, 6))

""" ================ Challenge 3 =================="""

"""
    In some online multiplayer games, there's a KDA ratio to evaluate a player's in-game performance:

    KDA=(k+a)/d

    k is how many players you took down.
    d is how many times you died.
    a is how many assists you had.
    Write a kda() function that takes in parameters: k, d, a.

    This function should calculate and return the KDA ratio that uses these paremeters.
"""
def kda(k, d, a):
  if d == 0:
    return "Undefined (deaths cannot be 0)"
  return (k + a) / d

print(kda(10, 2, 3))

""" ================ Challenge 4 =================="""

"""
    Why are there so many Moon emojis? Each one represents a different Moon phase, the shape of the Moon's sunlit portion as viewed from the Earth.

    Write a moon_phase() function that takes in a phase parameter of the Moon phase name given below and returns the correct Moon emoji for it:

    New Moon → 🌑
    Waxing Crescent → 🌒
    First Quarter → 🌓
    Waxing Gibbous → 🌔
    Full Moon → 🌕
    Waning Gibbous → 🌖
    Last Quarter → 🌗
    Waning Crescent → 🌘
    Else an invalid phase name is passed to moon_phase(), return 'Invalid moon phase'.

    Call the moon_phase() to test it out:

    answer = moon_phase('New Moon')
    print(answer)  

    # Output: 🌑
"""
def moon_phase(phase):
  if phase == "New Moon":
    return "🌑"
  elif phase == "Waxing Crescent":
    return "🌒"
  elif phase == "First Quarter":
    return "🌓"
  elif phase == "Waxing Crescent":
    return "🌔"
  elif phase == "Full Moon":
    return "🌕"
  elif phase == "Waning Gibbous":
    return "🌖"
  elif phase == "Last Quarter":
    return "🌗"
  elif phase == "Waning Crescent":
    return "🌘"
  else:
    return "Invaid Moon Phase"

answer = moon_phase("New Moon")
print (answer)

""" ================ Challenge 5 =================="""
"""
People say that every year of a dog's life is roughly equal to seven years of a human's life. 🥲

Write a dog_years() function that takes two parameters:

name (string)
age (integer)
It should calculate and return a string featuring the dog's name as well as its age in human years.

For example, if the dogs Landon, Red, and Cooper were 3, 6, and 2 years old respectively:

dog_years('Landon', 3)
dog_years('Red Bean', 6)
dog_years('Cooper', 2)

The return messages should look like:

Landon is 21 years old in human years.
Red Bean is 42 years old in human years.
Cooper is 14 years old in human years.

Note: Make sure your output matches what's in the code comments above.
""" 
def dog_years(name, age):
  human_years = age * 7
  return f"{name} is {human_years} years old in human years."

print(dog_years("Cooper", 7))
print(dog_years("Bailey", 6))
