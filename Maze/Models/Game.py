from abc import ABC, abstractmethod
#from mrx2d.Matrix import ObservableMatrix as Matrix
from Models.GameMatrix import GameMatrix;

class Game(ABC):
    def __init__(this):
        this.map = GameMatrix()
        this.drawer = None;

    @abstractmethod
    def Init(self):
        pass

    @abstractmethod
    def Loop(self) -> bool:
        pass

    @abstractmethod
    def End(self):
        pass

    def Start(this):
        this.Init()
        while this.Loop():
            pass
        this.End()