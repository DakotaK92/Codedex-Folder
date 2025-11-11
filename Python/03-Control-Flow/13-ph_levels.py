ph = int(input("Enter a pH level (0-14): "))

if ph > 7:
  print("basic")
elif ph < 7:
  print("acidic")
else:
  print("neutral")