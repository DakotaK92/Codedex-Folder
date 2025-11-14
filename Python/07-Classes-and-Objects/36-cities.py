class City:
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

dallas = City("Dallas", "USA", 1000000, ["Arlington Stadium", "American Airlanes", "Disco Ball Tower"])

print(vars(dallas))