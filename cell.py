from graphics import Line, Point

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win

    def draw(self, x1, y1, x2, y2):
        if self.__win is None:
            return
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.has_left_wall:
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x1, self.__y2)
            self.__win.draw_line(Line(p1, p2), "black")
        if self.has_top_wall:
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x2, self.__y1)
            self.__win.draw_line(Line(p1, p2), "black")
        if self.has_right_wall:
            p1 = Point(self.__x2, self.__y1)
            p2 = Point(self.__x2, self.__y2)
            self.__win.draw_line(Line(p1, p2), "black")
        if self.has_bottom_wall:
            p1 = Point(self.__x1, self.__y2)
            p2 = Point(self.__x2, self.__y2)
            self.__win.draw_line(Line(p1, p2), "black")

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"

        def midpoint(a, b):
            return (a + b) // 2

        p1 = Point(midpoint(self.__x1, self.__x2), midpoint(self.__y1, self.__y2))
        p2 = Point(midpoint(to_cell.__x1, to_cell.__x2), midpoint(to_cell.__y1, to_cell.__y2))

        self.__win.draw_line(Line(p1, p2), color)
