def get_item(x):
  if x == 1:
    return '🍔 Cheeseburger'
  elif x == 2:
    return '🍟 Fries'
  elif x == 3:
    return '🥤 Soda'
  elif x == 4:
    return '🍦 Ice Cream'
  elif x == 5:
    return '🍪 Cookie'
  else:
    return 'Invalid Number'

def welcome():
  print("Welcome to Whataburger!")
  print("Check out our menu!")
  print('🍔 Cheeseburger')
  print('🍟 Fries')
  print('🥤 Soda')
  print('🍦 Ice Cream')
  print('🍪 Cookie')

welcome()