class Restaurant:
  name = ''
  type = ''
  rating = 0.0
  delivery = False

bobs_burgers = Restaurant()
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.type = 'American Diner'
bobs_burgers.rating = 4.2
bobs_burgers.delivery = False

whataburger = Restaurant()
whataburger.name = "Whataburger"
whataburger.type = "Sit and Eat"
whataburger.rating = 5.0
whataburger.delivery = False

wendies = Restaurant()
wendies.name = "Wendies"
wendies.type = "Sit and Eat"
wendies.rating = 4.8
wendies.delivery = False

print(vars(bobs_burgers))
print(vars(whataburger))
print(vars(wendies))