from Models.CountdownTile import CountdownTile

class SnakeTile(CountdownTile):
    def __init__(self, lifetime : int):
        super().__init__((0, 255, 0), "@", lifetime)
    
    def onCountdownEnd(self): 
        self.delete()