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

    # to move right


    # to draw shape
    def draw_shape(self):

        for y in range(self.height):
            for x in range(self.width):
                if (self.shape[y][x] == 1):
                    pass

    # to erase shape
    def erase_shape(self):
        for y in range(self.height):
            for x in range(self.width):
                if (self.shape[y][x] == 1):
                    pass

    # can move if reaches to bottom of screen
    def can_move(self):
        result = True
        for x in range(self.width):
            # check if bottom is a 1
            if (self.shape[self.height-1][x] == 1):
                if :
                    result = False
        return result

    def rotate(self):
        # first erase the shape
        self.erase_shape(self)
        rotated_shape = []

        for b in range(7):
            pen.color(colors[b])
            screen_x, screen_y = self.x*20, self.y*20
            pen.goto(screen_x, screen_y+b*25)
            pen.stamp()

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

pen.color(self.color)
colors = ["black", "lightblue", "blue", "orange", "yellow", "green", "purple", "red"]

def draw_score(self, score):
    pen = turtle.Turtle()
    pen.color("blue")
    pen.hideturtle()
    pen.goto(0, 0)
    pen.write("Score: {}".format(score), move=False, align="left", font=("Arial", 24, "normal"))


wn.listen()
wn.inkeypress("a")
wn.inkeypress("d")
wn.inkeypress("space")

# set the score to 0
score = 0
draw_score(pen, score)

# main game loop

while True:
    wn.update()

    # Move the shape
    # open row
    # check for the bottom

    # check for collision wit next row

        # erase the current shape

        # move the shape by 1

        # draw the shape again

    # draw the screen
    draw_score(pen, score)

    time.sleep(delay)

#wn.mainloop()
