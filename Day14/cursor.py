from enum import Enum

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4

class Cursor:
    def __init__(self, pos_x, pos_y, array_width, array_height):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.array_width = array_width
        self.array_height = array_height
        self.last_move = None

    def move(self, direction):
        match direction:
            case Direction.NORTH:
                if self.pos_y > 0:
                    self.pos_y = self.pos_y - 1
                else:
                    print('Cannot move North!')
            case Direction.SOUTH:
                if self.pos_y < self.array_height-1:
                    self.pos_y = self.pos_y + 1
                else:
                    print('Cannot move South!')
            case Direction.WEST:
                if self.pos_x > 0:
                    self.pos_x = self.pos_x - 1
                else:
                    print('Cannot move West!')
            case Direction.EAST:
                if self.pos_x < self.array_width-1:
                    self.pos_x = self.pos_x + 1
                else:
                    print('Cannot move East!')
        self.last_move = direction

    def set(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def __str__(self):
        return 'Cursor at [' + str(self.pos_x) + ', ' + str(self.pos_y) + ']'