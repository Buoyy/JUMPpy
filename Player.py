class Player:
  def __init__(self, name, char):
    self.name = name
    self.char = char
    self.pos = 0
  def __str__(self):
    return f"{self.name}with gfx '{self.char}' at ({self.pos})"
  def update(self, new):
    self.pos += new