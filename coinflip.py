import random

class Coin:
  heads = 0
  tails = 0
  total = 0

  def flip(self):
    noOfFlips = None
    while(True):
      noOfFlips = input("How often do you want to flip the coin?\n")
      try:
        noOfFlips = int(noOfFlips)
        break
      except ValueError:
        print("Invalid input. Should be a number.")

    self.total = noOfFlips

    for i in range(noOfFlips):
      result = random.randint(0, 1)
      if (result == 0):
        self.heads += 1
      else:
        self.tails += 1

  def analysis(self):
    print("\nHeads was flipped", self.heads, "times.")
    print("Tails was flipped", self.tails, "times.\n")
    print("Percentages:")
    print("Heads:", round(self.heads/self.total*100, 1),"%")
    print("Tails:", round(self.tails/self.total*100, 1), "%")

testCoin = Coin()
testCoin.flip()
testCoin.analysis()