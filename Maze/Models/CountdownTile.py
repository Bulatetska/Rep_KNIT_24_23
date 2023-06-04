from Models.DynamicTile import DynamicTile
from abc import abstractmethod, ABCMeta

class CountdownTile(DynamicTile, metaclass=ABCMeta):
    def __init__(self,color, char, countdown):
        self.countdown = countdown
        super().__init__(color, char)

    def update(self):
        self.countdown -= 1
        if self.countdown <= 0:
            self.countdown = 0
            self.onCountdownEnd()
    
    @abstractmethod
    def onCountdownEnd(self):
        pass