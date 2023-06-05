from mrx2d.Tiles import TileConsole as Tile
from abc import ABC, ABCMeta, abstractmethod

class DynamicTile(Tile, metaclass=ABCMeta):
    '''
    Abstract class for dynamic tiles.
    Attributes:
        map(GameMatrix): Game map.
    Methods:
        update(self): Update this tile.
        delete(self): Delete this tile.
    '''
    def __init__(self, color: tuple, char: str):
        super().__init__(color, char)
        self.map = None
        self.pos = None

    def delete(self):
        '''
        Delete tile from map.
        '''
        del self.map[self.pos]
        self.map = None

    @abstractmethod
    def update(self):
        pass
