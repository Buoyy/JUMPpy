import time
import random
from Graphics import Graphics
from Player import Player

class GameHandling:
  def __init__(self, p1, p2, gfx):
    self.p1 = p1
    self.p2 = p2
    self.gfx = gfx
    self.state = True

  @staticmethod
  def load_time():
    return random.randrange(1, 3)
  def roll(self):
    return random.randint(0, 6)
  def check(self):
    if self.p1.pos >= self.gfx.length-1:
      print(self.p1.name, " wins!")
      print(self.p2.name, " was behind by ", abs(self.gfx.length-1-self.p2.pos), "units.")
      self.state = False
      time.sleep(2)
      input("Thanks for playing!")
    elif self.p2.pos >= self.gfx.length-1:
      print(self.p2.name, " wins!")
      print(self.p1.name, " was behind by ", abs(self.gfx.length-1-self.p1.pos), "units.")
      self.state = False
      time.sleep(2)
      input("Thanks for playing!")
    elif self.p1.pos == self.gfx.length-1 and self.p2.pos == self.gfx.length-1:
      print("It's a draw!!")
      self.state = False
      time.sleep(2)
      input("Thanks for playing!")


  def run(self):
    while True:
      print(self.p1.name, "'s turn.")
      input("Roll!: ")
      print("    Rolling...")
      time.sleep(0.5)
      roll1 = self.roll()
      print("You rolled", roll1, ".")
      print(self.p2.name, "'s turn.")
      input("Roll!: ")
      print("    Rolling...")
      time.sleep(0.5)
      roll2 = self.roll()
      print("You rolled", roll2, ".")
      time.sleep(0.1)
      input('Continue?: ')
      self.gfx.clear()
      self.p1.update(roll1)
      self.p2.update(roll2)
      self.check()
      if (not self.state):
        break
      Graphics.clear()
      self.gfx.update(self.p1, self.p2)
      self.gfx.display()

def start():
  #This variable gives more depth to the loading times. Will remain constant for one playthrough. 
 load = GameHandling.load_time()

 input("(hit enter for next dialog box at all stages of the game)")
 Graphics.clear()
 time.sleep(load)
 print("Hello! \nWelcome to JUMP!!")

 input()

 print("\n\nThis is a 2 player game which resulted due to experiments with multiple script handling and module usage.")

 input()

 print("\n\n\n\nINSTRUCTIONS:\nTo roll the dice, just hit the Enter/Return key. ")
 input("Once ready to play, hit Enter/Return.")


def init():
  #creating the Player objects
 name1 = input("Enter 1st player's name: ")
 char1 = input("Enter 1st player's character: ")
 name2 = input("Enter 2nd player's name: ")
 char2 = input("Enter 2nd player's character: ")
 length = int(input("Enter the length of the road: "))
 Graphics.clear()
 time.sleep(0.5)
 print("Done. ")
 p1, p2 = Player(name1, char1), Player(name2, char2)
 print("Loading...")
 time.sleep(2)
 Graphics.clear()
 time.sleep(0.5)
 gfx = Graphics(length)
 gfx.update(p1, p2)
 return GameHandling(p1, p2, gfx)