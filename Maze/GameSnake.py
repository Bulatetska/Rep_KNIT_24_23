from enum import Enum
from Models.Game import Game
from Models.SnakeTile import SnakeTile
from mrx2d.Drawers import ConsoleDrawer as Drawer
from mrx2d.Tiles import TileConsole as Tile


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class GameSnake(Game):
    def Init(self):
        self.snakePos = (25,25)
        self.snakeLength = 1
        self.direction = Direction.UP
        self.drawer = Drawer(self.map)
        self.drawer.drawAll()
        #fill the map with initial tiles (black border # 50*50)
        for i in range(0,50):
            for j in range(0,50):
                if i == 0 or j == 0 or i == 49 or j == 49:
                    self.map[(i,j)] = Tile((0,0,0), "#")
        
        self.map[self.snakePos] = SnakeTile(self.snakeLength)

    def Loop(self): # TODO: Implement
        pass

    def End(self):
        print("        GAME OVER       ")
        print("╔══════════════════════╗")
        print("║                      ║")
        print("║    Snake Game Result ║")
        print("║                      ║")
        print("╠══════════════════════╣")
        print("║                      ║")
        print("║      Score: {:>6}   ║".format(self.score))
        print("║                      ║")
        print("╚══════════════════════╝")

    def GetInput(self): # TODO: Implement
        pass

    def NextPos(self) -> tuple: # TODO: Implement
        pass
