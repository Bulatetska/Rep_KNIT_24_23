from abc import ABC, abstractmethod
#from mrx2d.Matrix import ObservableMatrix as Matrix
from Models.GameMatrix import GameMatrix;
import time

class Game(ABC):
    '''
    Абстрактний клас гри. 
    Attributes:
        map (Matrix): Матриця для мапи.
        drawer (Drawer): Drawer для відображения матриці.
    Methods:
        Init(): Ініціалізація гри.
        Loop(): Основний цикл гри.
        End(): Завершення гри.
        Start(): Запуск гри. Ініціалізація і запуска основного циклу.
    '''
    def __init__(this):
        this.map = GameMatrix(2)
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
            time.sleep(0.3)
        this.End()