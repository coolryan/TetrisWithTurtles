"""
    Filename: tetris_model.py
    Author: Ryan Setaruddin
    purpose: To design a game called Tetris
    This will represents the game
    Date: Feb, 19, 2024
"""
import turtle
import time
import random

# turtle size default is 20x20
# setup window screen
wn = turtle.Screen()
wn.title("TETRIS BY Ryan Setaruddin")
wn.bgcolor("black")
wn.setup(width=600, height=800)
wn.tracer(0)

delay = 0.1

class Block:
    """docstring for Block"""
    def __init__(self, x: int = 0, y: int = 0, color: str = "black", speed: int = 0):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed

    def draw(self):
        raise NotImplementedError

class Shape(Block):
    """docstring for Shape"""
    # to draw the Shape
    def __init__(self):
        # Block Shape
        square = [[1,1],
                [1,1]]

        horizontal_line = [[1,1,1,1]]

        vertical_line = [[1],
                        [1],
                        [1],
                        [1]]

        left_l = [[1,0,0,0],
                [1,1,1,1]]

        right_l = [[0,0,0,1],
                [1,1,1,1]]

        left_s = [[1,1,0],
                [0,1,1]]

        right_s = [[0,1,1],
                [1,1,0]]

        t = [[0,1,0],
            [1,1,1]]

        shapes = [square, horizontal_line, vertical_line, left_l, right_l, left_s, right_s, t]

        # choose a random shape each time
        self.shape = random.choice(shapes)

        self.height = len(self.shape)
        self.width = len(self.shape[0])

    # to move left
    def move_left(self, grid):
        if self.x > 0:
            if grid[self.y][self.x - 1] == 0:
                self.erase_shape(grid)
                self.x -= 1

    # to move right
    def move_right(self, grid):
        if self.x < 12 - self.width:
            if grid[self.y][self.x + self.width]== 0:
                self.erase_shape(grid)
                self.x += 1

    # to draw shape
    def draw_shape(self, grid):
        for h in range(self.height):
            for w in range(self.width):
                if (self.shape[h][w] == 1):
                    grid[self.y + h][self.x + w] = self.color

    # to erase shape
    def erase_shape(self, grid):
        for h in range(self.height):
            for w in range(self.width):
                if (self.shape[h][w] == 1):
                    grid[self.y + h][self.x + w] = 0

    # can move if reaches to bottom of screen
    def can_move(self. grid):
        result = True
        for w in range(self.width):
            # check if bottom is a 1
            if (self.shape[self.height-1][w] == 1):
                if (grid[self.y + self.height][self.x + w] != 0):
                    result = False
        return result

    def rotate(self, grid):
        # first erase the shape
        self.erase_shape(grid)
        rotated_shape = []

        for s in range(len(self.shape[0])):
            new_row = []
            for ls in range(len(self.shape)-1, -1, -1):
                new_row.append(self.shape[ls][s])
            rotated_shape,append(new_row)

            right_side = self.x + len(rotated_shape[0])

            if right_side < len(grid[0]):
                self.shape = rotated_shape
                # update the height and width
                self.height = len(self.shape)
                self.width = len(self.shape[0])

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

class Tetris:
    """docstring for Tetris"""
    def __init__(self, upcomingBlockstate: list[Block], fallingBlockState: list[Block], existingBlockState: list[Block], score: int = 0):
        self.upcomingBlockstate = upcomingBlockstate
        self.fallingBlockState = fallingBlockState
        self.existingBlockState = existingBlockState
        self.score = score

# create the drawing pen
pen = turtle.Turtle()
pen.penup()
pen.speed(self.speed)
pen.shape("square")
pen.setundbuffer(None)

# draw grid
def draw_grid(self):
    pen.clear()
    top, left = self.x, self.y

    colors = ["black", "lightblue", "blue", "orange", "yellow", "green", "purple", "red"]
    
    for g in range(len(grid)):
        for lg in range(len(grid[0])):
            screen_x, screen_y = left + (lg * 20), top - (g * 20)
            color_number = grid[lg][g]
            color = colors[color_number]
            pen.color(color)
            pen.goto(screen_x, screen_y)
            pen.stamp()

# check the grid
def check_grid(self):
    # check if each row is full
    y = 23
    while y > 0:
        is_full = True
        for x in range(0, 12):
            if grid[y][x] == 0:
                is_full = False
                y -= 1
                break
        if is_full:
            global score
            score += 10
            draw_score(pen, score)
            for copy_y in range(y, 0, -1):
                for copy_x in range(0, 12):
                    grid[copy_y][copy_x] = grid[copy_y-1][copy_x]

# draw the score
def draw_score(pen, score):
    pen.color("blue")
    pen.hideturtle()
    pen.goto(self.x, self.y)
    pen.write("Score: {}".format(score), move=False, align="left", font=("Arial", 24, "normal"))

# create †he basic shape for the start of the game
shape = Shape()

# put the shape in the grid
grid[shape.y][shape.x] = shape.color

# draw the inital grid
draw_grid(pen, grid)

# to have control panels
wn.listen()
wn.inkeypress(lambda: shape.move_left(grid), "a")
wn.inkeypress(lambda: shape.move_right(grid), "d")
wn.inkeypress(lambda: shape.rotate(grid), "space")

# set the score to 0
score = 0
draw_score(pen, score)

# main game loop
while True:
    wn.update()

    # Move the shape
    # open row
    # check for the bottom
    if shape.y == 23 - shape.height + 1:
        shape = Shape()
        check_grid(grid)

    # check for collision with next row
    elif shape.can_move(grid):
        # erase the current shape
        shape.erase_shape(grid)

        # move the shape by 1
        shape.y += 1

        # draw the shape again
        shape.draw_shape(grid)

    else:
        shape = Shape()
        check_grid(grid)

    # draw the screen
    draw_grid(pen, grid)
    draw_score(pen, score)

    time.sleep(delay)

#wn.mainloop()
