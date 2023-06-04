from enum import Enum
from Models.FoodTile import FoodTile
from Models.Game import Game
from Models.GameMatrix import GameMatrix
from Models.SnakeTile import SnakeTile
from mrx2d.Drawers import ConsoleDrawer as Drawer
from mrx2d.Tiles import TileConsole as Tile
import random
import msvcrt

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class GameSnake(Game):
    def Init(self):
        self.score = 0
        self.snakePos = (25,25)
        self.snakeLength = 1
        self.direction = Direction.UP
        #Намалювати стіну
        for i in range(0,50):
            for j in range(0,50):
                if i == 0 or j == 0 or i == 49 or j == 49:
                    self.map[(i,j)] = Tile((255,255,255), "#")
                else:
                    self.map[(i,j)] = Tile((0,0,0), " ")
        #Створити змійку
        self.GenerateFood()
        self.drawer = Drawer(self.map)
        self.map[self.snakePos] = SnakeTile(self.snakeLength)
        self.drawer.drawAll()

    def GenerateFood(self):
        while True:
            foodPos = (random.randint(1,48), random.randint(1,48))
            if self.map[foodPos].char == " ":
                self.map[foodPos] = FoodTile()
                break

    def Loop(self):
        self.map.Update()
        self.GetInput()
        next_pos = self.NextPos()
        next_tile = self.map[next_pos]

        if isinstance(next_tile, SnakeTile) or next_tile.char == "#":
            return False

        if isinstance(next_tile, FoodTile):
            self.score += 10
            self.snakeLength += 1
            next_tile.delete()
            self.GenerateFood() 

        self.map[next_pos] = SnakeTile(self.snakeLength)
        self.snakePos = next_pos
        self.GenerateFood()
        return True

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

    def GetInput(self): 
        if msvcrt.kbhit():
            key = msvcrt.getch()
            key = key.decode("utf-8").upper()
            
            if key == 'W':
                self.direction =  Direction.UP
            elif key == 'S':
                self.direction = Direction.DOWN
            elif key == 'A':
                self.direction = Direction.LEFT
            elif key == 'D':
                self.direction = Direction.RIGHT

    def NextPos(self) -> tuple: 
            if  self.direction == Direction.DOWN:
                nextPos = (self.snakePos[0] + 1, self.snakePos[1])
            elif self.direction == Direction.UP:
                nextPos = (self.snakePos[0] - 1, self.snakePos[1])
            elif self.direction == Direction.LEFT:
                nextPos = (self.snakePos[0], self.snakePos[1] - 1)
            elif self.direction == Direction.RIGHT:
                nextPos = (self.snakePos[0], self.snakePos[1] + 1)
            return nextPos
