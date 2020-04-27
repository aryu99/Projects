"""
Clone of 2048 game.
"""

import poc_2048_gui
import random
# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    result = []        
    
    for num in line:
        if num != 0:
            result.append(num)

    if len(result) < len(line):
        while len(result) < len(line):
            result.append(0)
    # print (result)
    if len(result) <= 2:
        try:
            if result[0] == result[1]:
                result[0] = result[0] + result[1]
                result[1] = 0
                # print (type(result))
                return result
            else:
                return result
        except:
            return result
    print(result)
    i = 0
    while (i + 1) <= (len(line)-1): # if i +
        if result[i] == result[i + 1] and result[i] != 0:
            result.append(0)
            result[i] = result[i] + result[i + 1]
            print("before loop: ", result)
            x = 0
            for n in range((len(line) - 1) - i):             
                result[i + 1 + x] = result[i + 2 + x]
                x += 1
                print ("loop: ",result)
        else:
            pass
        i += 1
   
    while len(result) > len(line):
        result.pop()

    print ("the result is:" ,result)
    return result



class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self._move = {UP: [], DOWN: [], RIGHT: [], LEFT: []}
        for col in range(self._width):
            self._move[UP].append((0, col))
            self._move[DOWN].append((self._height - 1, col))
        for row in range(self._height):
            self._move[LEFT].append((row, 0))
            self._move[RIGHT].append((row, self._width - 1))



        # self.reset()


    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        
        self._grid = [[0 for col in range(self._width)] for row in range(self._height)]
        i = 0
        while i < 2:
            self.new_tile()
            i += 1
        print "The grid is: " + str(self._grid)

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        change = False
        if direction == UP or DOWN:
            line_length = self._height
        else:
            line_length = self._width
        
        for init_tile in self._move[direction]:
            line = [self.get_tile(init_tile[0] + num*OFFSETS[direction][0], init_tile[1] + num*OFFSETS[direction][1]) 
                        for num in range(line_length)]
            new_line = merge(line)

            if new_line != line:
                change = True

            for num in range(line_length):
                self.set_tile(init_tile[0] + num*OFFSETS[direction][0], init_tile[1] + num*OFFSETS[direction][1], new_line[num])

        if change:
            print "new tile"
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        x = random.randrange(0, self._width)
        y = random.randrange(0, self._height)
        print "Col is: " + str(x) + "  " + "Row is: " + str(y)
        if self._grid[y][x] == 0:
            
            
            
            if random.randint(1, 100) <= 90:
                val = 2
            else:
                val = 4
        
            self._grid[y][x] = val
        else:
            self.new_tile

        



    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
