
class Bitmap:
    def __init__(self, n, m):
        self.__column = n
        self.__row = m
        self.__matrix = [["O" for x in range(self.__column)] for y in range(
            self.__row)]

    def colour_pixels(self, column, row, c):
        column, row = self._set_vars(column, row,)
        self.__matrix[row][column] = c

    def draw_vertical_segment(self, column, row1, row2, c):
        column, row1 = self._set_vars(column, row1,)
        for y in range(row1, row2):
            self.__matrix[y][column] = c

    def draw_horizontal_segment(self, row, column1, column2, c):
        row, column1 = (self._set_vars(row, column1))
        for x in range(column1, column2):
            self.__matrix[row][x] = c

    def show_contents(self):
        for row in range(self.__row):
            print("".join([x for x in self.__matrix[row]]))
        print("\n")

    def clear(self):
        self.__matrix = [["O" for x in range(self.__column)] for y in range(
            self.__row)]

    def _set_vars(self, *args):
        var_tuple = [value - 1 for value in args]
        return tuple(var_tuple)
