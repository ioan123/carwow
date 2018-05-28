import re
from bitmap import Bitmap
from commands import *
import Queue
import logging
logging.basicConfig(level=logging.INFO)


class WrongCommandException():
    pass


def file_check(input_file):
    """Parsing the input file and checking the validity of each command."""
    log = logging.getLogger(__name__)
    f_in = open(input_file, "r")
    commands = Queue.Queue()

    for line in f_in:
        try:
            command = re.match("^[A-Z]{1}", line).group()
        except AttributeError:
            log.error("Bad command format at line: %s", line)
            raise

        if not command:
            raise WrongCommandException("Bad command: ", line)

        elif command == CREATE_BITMAP:
            args = re.match("^\s([0-9]{1,3})\s([0-9]{1,3})\n?$", line[1:])
            assert args is not None, "Wrong command format for bitmap creation."

            n, m = (int(args.group(1)), int(args.group(2)),)
            assert n >= 1 and n <= 255, "Expecting a number between 1-255"
            assert m >= 1 and m <= 255, "Expecting a number between 1-255"
            commands.put({command: [n, m]})

        elif command == COLOUR_PIXEL:
            args = re.match("^\s([0-9]{1,3})\s([0-9]{1,3})\s([A-Z]{1})\n?$", line[1:])
            assert args is not None, "Wrong command format for colouring pixel."

            x, y, c = (int(args.group(1)), int(args.group(2)), str(args.group(3)),)
            assert x >= 1 and x <= n, "X coordinates out of range. (1 < x <= n)"
            assert y >= 1 and y <= m, "Y coordinates out of range. (1 < y <= m)"
            commands.put({command: [x, y, c]})

        elif command == VERTICAL_SEGMENT:
            args = re.match("^\s([0-9]{1,3})\s([0-9]{1,3})\s([0-9]{1,3})\s([A-Z]{1})\n?$", line[1:])
            assert args is not None, "Wrong command format for drawing vertical segment."

            x, y1, y2, c = (int(args.group(1)), int(args.group(2)),
                            int(args.group(3)), str(args.group(4)),)
            assert x >= 1 and x <= n, "X coordinates out of range. (1 < x <= n)"
            assert y1 >= 1 and y1 <= m, "Y coordinates out of range. (1 < y1 <= m)"
            assert y2 >= 1 and y2 <= m, "Y coordinates out of range. (1 < y2 <= m)"
            assert y1 <= y2, "Y2 coordinates out of range. (y1 <= y2 )"
            commands.put({command: [x, y1, y2, c]})

        elif command == HORIZONTAL_SEGMENT:
            args = re.match("^\s([0-9]{1,3})\s([0-9]{1,3})\s([0-9]{1,3})\s([A-Z]{1})\n?$", line[1:])
            assert args is not None, "Wrong command format for drawing horizontal segment."
            x1, x2, y, c = (int(args.group(1)), int(args.group(2)),
                            int(args.group(3)), str(args.group(4)),)

            assert y >= 1 and y <= m, "Y coordinates out of range. (1 < y <= m)"
            assert x1 >= 1 and x1 <= n, "Y coordinates out of range. (1 < x1 <= n)"
            assert x2 >= 1 and x2 <= n, "Y coordinates out of range. (1 < x2 <= n)"
            assert x1 <= x2, "X2 coordinates out of range. (x1 <= x2 )"
            commands.put({command: [y, x1, x2, c]})

        elif command == CLEAR_TABLE:
            args = re.match("^C\n?$", line)
            assert args is not None, "Wrong command format for clearing contents."
            commands.put({command: []})

        elif command == SHOW_CONTENTS:
            args = re.match("^S\n?$", line)
            assert args is not None, "Wrong command format for showing contents."
            commands.put({command: []})
        else:
            raise WrongCommandException("Command not found.", line)

    f_in.close()
    return commands
