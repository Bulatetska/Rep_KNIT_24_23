from mrx2d.Tiles import TileConsole as Tile
from abc import ABC, ABCMeta, abstractmethod

class DynamicTile(Tile, metaclass=ABCMeta):
    def __init__(self, color: tuple, char: str):
        super().__init__(color, char)
        self.map = None

    
    @abstractmethod
    def update(self):
        pass
