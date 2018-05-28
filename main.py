#!/usr/bin/env python2
from parser import file_check
from bitmap import Bitmap
from commands import *


def main():
    """Main function."""
    commands = file_check("input.txt")
    bitmap = None
    while not commands.empty():
        for k, v in commands.get().items():
            if k == CREATE_BITMAP:
                bitmap = Bitmap(v[0], v[1])
            if k == SHOW_CONTENTS:
                bitmap.show_contents()
            if k == COLOUR_PIXEL:
                bitmap.colour_pixels(v[0], v[1], v[2])
            if k == VERTICAL_SEGMENT:
                bitmap.draw_vertical_segment(v[0], v[1], v[2], v[3])
            if k == HORIZONTAL_SEGMENT:
                bitmap.draw_horizontal_segment(v[0], v[1], v[2], v[3])
            if k == CLEAR_TABLE:
                bitmap.clear()


if __name__ == "__main__":
    main()
