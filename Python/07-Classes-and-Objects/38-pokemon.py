# Write code below 💖

class Pokemon:
  def __init__ (self, entry, name, types, description, level, region, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.level = level
    self.region = region
    self.is_caught = is_caught

  def speak(self):
    print(self.name + ', ' + self.name + '!')

  def display_details(self):
    print("Entry Number: " + str(self.entry))
    print("Name: " + self.name)

    if len(self.types) == 1:
      print("Type: " + self.types[0])
    else:
      print("Type: " + self.types[0] + "/" + self.types[1])

    print('Lv. ' + str(self.level))
    print('Region: ' + self.region)
    print('Description: ' + self.description)

    if self.is_caught:
      print(self.name + ' has already been caught')
    else:
      print(self.name + ' hasn\'t already been caught')

pickachu = Pokemon(25, "Pikachu", ["Electric"], "It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.", 25, "Kanto", True)
gengar = Pokemon(94, "Gengar", ["Ghost", "Poison"], "On the night of a full moon, if shadows move on their own and laugh, it must be Gengar's doing.", 30, "Kanto", False)
lugia = Pokemon(249, "Lugia", ["Psychic", "Flying"], "It is said that it quietly spends its time deep at the bottom of the sea because its wings can create a 40-day storm.", 70, "Johto", False)

pickachu.speak()
gengar.speak()
lugia.speak()