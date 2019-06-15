import random

class Die:
  faces = 0

  def __init__(self, faces = 6):
    self.faces = faces

  def roll(self):
    print(random.randint(1, self.faces))

class ColourDie(Die):
  colour = None

  def __init__(self, colour, faces = 6):
    super().__init__(faces)
    self.colour = colour

  def get_colour(self):
    print(self.colour)

print("Normal die throw:")
testDie = Die(12)
testDie.roll()

print()
print("Colourful die throw:")
testColourDie = ColourDie("Red", 42)
testColourDie.get_colour()
testColourDie.roll()