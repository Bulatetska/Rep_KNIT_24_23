from abc import abstractmethod


class Tile:
    def __init__(self) -> None:
        self.collider = None
    @abstractmethod
    def getViewData(self)->object:
        pass

class TileConsole(Tile):
    def __init__(self, color:tuple, char:str, collider = True):
        if len(color) != 3:
            raise ValueError("Color must be a tuple of 3 ints")
        self.color = color
        self.char = char
        self.collider = collider
        
    @staticmethod
    def colored(r, g, b, text):
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
    
    def getViewData(self):
        return self.colored(self.color[0], self.color[1], self.color[2], self.char)