import os

class Graphics:
  def __init__(self, length):
    self.length = length
    self.road1 = ['-']*length
    self.road2 = ['-']*length
  def display(self):
    print('\n', ' ', end='')
    for i in self.road1:
      print(i, end=' ')
    print('\n\n','# '*(self.length+1),'\n', end='')
    
    print('\n', ' ', end='')
    for i in self.road2:
      print(i, end=' ')
    print()

  @staticmethod
  def clear():
    os.system('cls' if os.name=='nt' else 'clear')

  def update(self, p1, p2):
    self.road1 = ['-']*self.length
    self.road2 = ['-']*self.length
    self.road1[p1.pos] = p1.char
    self.road2[p2.pos] = p2.char