from graphics import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    num_rows = 10
    num_cols = 10
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = 20
    cell_size_y = 20
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)

    win.wait_for_close()
main()
