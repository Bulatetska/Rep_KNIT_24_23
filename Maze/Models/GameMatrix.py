from mrx2d.Matrix import ObservableMatrix as Matrix
from mrx2d.Tiles import TileConsole
from DynamicTile import DynamicTile

class GameMatrix(Matrix):
    def __init__(self,dim , data = []):
        super().__init__(dim, data)
        self._update_list = []
    
    def __setitem__(self, idx: tuple, value : TileConsole):
        if isinstance(value, DynamicTile):
            self._update_list.append(value)
            value.map  = self
        return super().__setitem__(idx, value)
    
    def __delitem__(self, idx: tuple):
        if isinstance(self[idx], DynamicTile):
            self._update_list.remove(self[idx])
            self[idx].map = None
        return super().__delitem__(idx)
    
    def set_data(self, data):
        for tile in self._update_list:
            tile.map = None
        self._update_list = []
        
        for tile in data:
            if isinstance(tile, DynamicTile):
                self._update_list.append(tile)
                tile.map  = self

        return super().set_data(data)

    def update(self):
        for tile in self._update_list:
            tile.update()