from mrx2d.Matrix import ObservableMatrix as Matrix
from mrx2d.Drawers import ConsoleDrawer as Drawer
from mrx2d.Tiles import TileConsole as Tile
import maze_tools

#Чорна магія матриць
level_map = Matrix(3)
output_matrix = Matrix(2)


# THE TEST DELETE LATER
for x in [
    (a, b, c)
    for a in range(0, 50)
    for b in range(0, 50)
    for c in range(0, 50)
]:
    level_map[x] = Tile(tuple([x[0]*4,x[1]*4,x[2]*4]), "#")

output_matrix = level_map[tuple([10])]
# END OF THE TEST

drawer = Drawer(output_matrix)
drawer.drawAll()
for i in range(0, 50):
    output_matrix.set_data(level_map[tuple([i])]._data)
    #time.sleep(0.05)
