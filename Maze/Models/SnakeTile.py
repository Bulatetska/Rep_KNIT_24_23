import CountdownTile

class SnakeTile(CountdownTile):
    def __init__(lifetime : int):
        super().__init__((0, 255, 0), "@")
    
    def onCountdownEnd(): #TODO: Implement this
        pass