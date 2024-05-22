"""
    Filename: tetris_model.py
    Author: Ryan Setaruddin
    purpose: To design a game called Tetris
    This will represents the game
    Date: Feb, 19, 2024
"""

# import libraries
import random
import time
from turtle import Screen, Turtle

# import py file
from constants import BLOCK_HEIGHT, ShapeType, COLOR

delay = 0.1

# Block class
class Block:
    """docstring for Block"""
    # constructor
    def __init__(self, x: int = 0, y: int = 0, color: COLOR = COLOR.BLACK, speed: int = 0):
        self.x, self.y = x, y
        self.color = color.value
        self.speed = speed
        self.height = BLOCK_HEIGHT

    # draw method
    def draw(self, pen):
        pen.penup()
        pen.hideturtle()  

        pen.color(self.color)
        pen.fillcolor(self.color)

        pen.begin_fill()

        pX, pY = self.x, self.y
        pen.goto(pX, pY)
        pen.down()

        pX += BLOCK_HEIGHT
        pen.goto(pX, pY)
        pY += BLOCK_HEIGHT
        pen.goto(pX, pY)

        pX -= BLOCK_HEIGHT
        pen.goto(pX, pY)
        pY -= BLOCK_HEIGHT
        pen.goto(pX, pY)

        pen.end_fill()

# Shape class
class Shape:
    """docstring for Shape"""
    # constructor
    def __init__(self, x: int, y: int, shapeType: type, color: COLOR | None = None):
        # Block Shape
        self.listOfBlocks = []
        self.color = color
        self.shapeType = shapeType
        self.x, self.y = x, y
        self.speed = 5
        self.initiate_shape()

    # initiate shape method
    def initiate_shape(self):
        """ Create the list of blocks according to its shape type """
        if self.shapeType == ShapeType.I_TETROMINO:
            color = self.color if self.color else COLOR.RED
            self.listOfBlocks.append(Block(self.x, self.y, color, self.speed+5))
            self.listOfBlocks.append(Block(self.x, self.y+BLOCK_HEIGHT, color, self.speed))
            self.listOfBlocks.append(Block(self.x, (self.y+BLOCK_HEIGHT*2), color, self.speed))
            self.listOfBlocks.append(Block(self.x, (self.y+BLOCK_HEIGHT*3), color, self.speed))
            self.listOfBlocks.append(Block(self.x, (self.y+BLOCK_HEIGHT*4), color, self.speed))

        elif self.shapeType == ShapeType.O_TETROMINO:
            color = self.color if self.color else COLOR.YELLOW
            self.listOfBlocks.append(Block(self.x, self.y, color, self.speed))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT, self.y, color, self.speed))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT, self.y-BLOCK_HEIGHT, color, self.speed))
            self.listOfBlocks.append(Block(self.x, self.y-BLOCK_HEIGHT, color, self.speed))

        elif self.shapeType == ShapeType.T_TETROMINO:
            color = self.color if self.color else COLOR.GREEN
            self.listOfBlocks.append(Block(self.x, self.y, color, self.speed))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT, self.y, color, self.speed))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT*2, self.y, color, self.speed))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT, self.y+BLOCK_HEIGHT, color, self.speed))

        elif self.shapeType == ShapeType.L_TETROMINO:
            color = self.color if self.color else COLOR.BLUE
            self.listOfBlocks.append(Block(self.x, self.y, color, self.speed))
            self.listOfBlocks.append(Block(self.x, self.y-BLOCK_HEIGHT, color, self.speed))
            self.listOfBlocks.append(Block(self.x, self.y-BLOCK_HEIGHT*2, color, self.speed))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT, self.y-BLOCK_HEIGHT*2, color, self.speed))

        elif self.shapeType == ShapeType.J_TETROMINO:
            color = self.color if self.color else COLOR.ORANGE
            self.listOfBlocks.append(Block(self.x, self.y, color, self.speed))
            self.listOfBlocks.append(Block(self.x, self.y-BLOCK_HEIGHT, color, self.speed))
            self.listOfBlocks.append(Block(self.x, self.y-BLOCK_HEIGHT*2, color, self.speed))
            self.listOfBlocks.append(Block(self.x-BLOCK_HEIGHT, self.y-BLOCK_HEIGHT*2, color, self.speed))

        elif self.shapeType == ShapeType.S_TETROMINO:
            color = self.color if self.color else COLOR.PURPLE
            self.listOfBlocks.append(Block(self.x, self.y, color, self.speed))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT, self.y, color, self.speed))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT, self.y+BLOCK_HEIGHT, color, self.speed))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT*2, self.y+BLOCK_HEIGHT, color, self.speed))

        elif self.shapeType == ShapeType.Z_TETROMINO:
            color = self.color if self.color else COLOR.PINK
            self.listOfBlocks.append(Block(self.x, self.y, color, self.speed))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT, self.y, color, self.speed))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT, self.y-BLOCK_HEIGHT, color, self.speed))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT*2, self.y-BLOCK_HEIGHT, color, self.speed))

    # draw method
    def draw(self, pen):  
        # Go through the shape's blocks and draw them.
        for block in self.listOfBlocks:
            block.draw(pen)

    # move method
    def move(self):
        for block in self.listOfBlocks:
            block.y -= self.speed

# Tertis class
class Tetris:
    """docstring for Tetris"""
    # constructor
    def __init__(
        self,
        game_turtle: Turtle,
        game_window: Screen,
        upcomingShapeState: list[Shape],
        fallingShapeState: list[Shape],
        existingShapeState: list[Shape],
        score: int = 0,
    ):
        self.upcomingShapeState = upcomingShapeState
        self.fallingShapeState = fallingShapeState
        self.existingShapeState = existingShapeState
        self.score = score

        # turtle size default is 20x20
        # setup window screen
        window = game_window
        window.title("TETRIS BY Ryan Setaruddin")
        window.bgcolor("black")
        window.setup(width=600, height=800)
        window.tracer(0, 0)
        self.pen = game_turtle
        self.pen.speed(0)
        self.window = window

    # draw method
    def draw(self):
        for shape in self.fallingShapeState:
            shape.draw(self.pen)

    # score method
    def score(pen, score):
        pen.color("blue")
        pen.hideturtle()
        pen.goto(self.x, self.y)
        pen.write("Score: {}".format(score), move=False, align="left", font=("Arial", 24, "normal"))

    def move_blocks(self):
        for shape in self.fallingShapeState:
            shape.move()

    def start_game(self):
        global delay
        is_done = False
        count = 0
        while not is_done:
            self.window.clear()
            self.window.update()
            self.move_blocks()
            self.draw()
            time.sleep(delay)
            count += 1
            if count > 50:
                is_done = True
    

# to have control panels

# set the score to 0
# score = 0
# draw_score(pen, score)

# main game loop
# while True:
#     wn.update()

#     # Move the shape
#     # open row
#     # check for the bottom

#     # check for collision with next row
    
#         # erase the current shape

#         # move the shape by 1

#         # draw the shape again

#     # draw the screen
#     draw_score(pen, score)

#     time.sleep(delay)

#wn.mainloop()
