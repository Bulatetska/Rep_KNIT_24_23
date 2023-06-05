from mrx2d.Matrix import ObservableMatrix as Matrix
from mrx2d.Tiles import TileConsole
from Models.DynamicTile import DynamicTile

class GameMatrix(Matrix):
    '''
    Доповнення класу матриці для роботи з динамічнимими тайлами
    Methods:
        Update() : оновлення усіх доданих динамічних тайлів 
    '''
    def __init__(self,dim , data = {}, default_tile = TileConsole((0,0,0), ' ')):
        super().__init__(dim, data)
        self._update_list = []
        self.default_tile = default_tile
    
    def __setitem__(self, idx: tuple, value : TileConsole):
        if isinstance(value, DynamicTile):
            self._update_list.append(value)
            value.map  = self
            value.pos = idx
        return super().__setitem__(idx, value)
    
    def __delitem__(self, idx: tuple):
        x = self[idx]
        if isinstance(x, DynamicTile):
            self._update_list.remove(self[idx])
            self[idx].map = None
        super().__delitem__(idx)
        self[idx] = self.default_tile;
    

    def set_data(self, data):
        for tile in self._update_list:
            tile.map = None
        self._update_list = []
        
        for tile in data:
            if isinstance(tile, DynamicTile):
                self._update_list.append(tile)
                tile.map  = self

        return super().set_data(data)

    def Update(self):
        for tile in self._update_list:
            tile.update()