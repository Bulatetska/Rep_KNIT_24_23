from mrx2d.Matrix import ObservableMatrix as Matrix
from mrx2d.Drawers import ConsoleDrawer as Drawer
from mrx2d.Tiles import TileConsole as Tile
#Функції
def convert_to_2d_projection(world:Matrix):
    size = world.get_size()
    rows = size[0]
    cols = size[1]
    depth = size[2]
    projection = Matrix(2)#[[' ' for _ in range(cols)] for _ in range(rows)]

    for col in range(cols):
        for row in range(rows-1, -1, -1):
            for cell in range(len(world[row][col])-1, -1, -1):
                char = world[(row,col,cell)]
                if char != ' ':
                    projection[(row,col)] = char
                    break

    return projection

def initWorld(input:Matrix) -> Matrix:
    pass