from Graphics import Graphics
import GameHandling
import time

GameHandling.start()

#immersion using time.sleep() and "Loading.."
time.sleep(0.4)
Graphics.clear()
print("Loading...")
time.sleep(1)
Graphics.clear()
time.sleep(0.3)

#running the game
game = GameHandling.init()
game.gfx.display() #to show initial stage of roads 

game.run()

Graphics.clear()
del game

input("Enter to close the app..")