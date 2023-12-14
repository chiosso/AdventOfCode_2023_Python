from enum import Enum

## PROCESS INPUT ##

maze = open('Day10/input.txt', 'r').readlines()
for i in range(len(maze)):
    maze[i] = maze[i].rstrip()
path = [ ['.']*len(maze[0]) for i in range(len(maze))]

## OBJECT AND FUNCTIONAL MODEL ##

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT =4

class Cursor:
    def __init__(self, pos_x, pos_y, last_move):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.last_move = last_move

    def move(self, direction):
        match direction:
            case Direction.UP:
                if self.pos_y > 0:
                    self.pos_y = self.pos_y - 1
                else:
                    print('Cannot move up!')
            case Direction.DOWN:
                if self.pos_y < len(maze)-1:
                    self.pos_y = self.pos_y + 1
                else:
                    print('Cannot move down!')
            case Direction.LEFT:
                if self.pos_x > 0:
                    self.pos_x = self.pos_x - 1
                else:
                    print('Cannot move left!')
            case Direction.RIGHT:
                if self.pos_x < len(maze[0])-1:
                    self.pos_x = self.pos_x + 1
                else:
                    print('Cannot move right!')
        self.last_move = direction

    def __str__(self):
        return 'Cursor at [' + str(self.pos_x) + ', ' + str(self.pos_y) + ']'

def nextMove(cursor, maze):
    match maze[cursor.pos_y][cursor.pos_x]:
        case '|':
            if cursor.last_move in [Direction.UP, Direction.DOWN]:
                return cursor.last_move
            else:
                print('Bad move!')
        case '-':
            if cursor.last_move in [Direction.LEFT, Direction.RIGHT]:
                return cursor.last_move
            else:
                print('Bad move!')
        case 'L':
            match cursor.last_move:
                case Direction.LEFT:
                    return Direction.UP
                case Direction.DOWN:
                    return Direction.RIGHT
                case _:
                    print('Bad move!')
        case 'J':
            match cursor.last_move:
                case Direction.RIGHT:
                    return Direction.UP
                case Direction.DOWN:
                    return Direction.LEFT
                case _:
                    print('Bad move!')
        case '7':
            match cursor.last_move:
                case Direction.RIGHT:
                    return Direction.DOWN
                case Direction.UP:
                    return Direction.LEFT
                case _:
                    print('Bad move!')
        case 'F':
            match cursor.last_move:
                case Direction.LEFT:
                    return Direction.DOWN
                case Direction.UP:
                    return Direction.RIGHT
                case _:
                    print('Bad move!')
        case _:
            return None

## TRAVERSE THE MAZE! ##

starting_positions=[(110,119,Direction.UP), (110,121,Direction.DOWN)]

for starting_position in starting_positions:
    cursor = Cursor(starting_position[0],starting_position[1],starting_position[2])
    print('Starting at [' + maze[cursor.pos_y][cursor.pos_x] + ']')
    steps_taken = 1
    path[cursor.pos_y][cursor.pos_x] = steps_taken
    while True:
        next_move = nextMove(cursor, maze)
        if (next_move == None):
            print('No more moves')
            break
        cursor.move(next_move)
        steps_taken = steps_taken + 1
        if maze[cursor.pos_y][cursor.pos_x] in ('S', '.'):
            print('Stopping at [' + maze[cursor.pos_y][cursor.pos_x] + ']')
            break
        print('Moved ' + str(next_move) + ', got to [' +  maze[cursor.pos_y][cursor.pos_x] + '], taken ' + str(steps_taken) + ' steps')
        if path[cursor.pos_y][cursor.pos_x] != '.':
            if path[cursor.pos_y][cursor.pos_x] <= steps_taken:
                print('Met with another path, stopping here')
                break
        path[cursor.pos_y][cursor.pos_x] = steps_taken

## FIND THE FARTHEST POINT ##

farthest_steps = 0
for line in path:
    for n in line:
        if type(n) == int:
            if n > farthest_steps:
                farthest_steps = n

print('Farthest point: ' + str(farthest_steps))

## OUTPUT THE PATH ##

output = open('Day10/output.txt', 'w')
for line in path:
    output.write(str(line))
output.close()