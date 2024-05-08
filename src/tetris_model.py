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
import turtle

# import py file
from constants import BLOCK_HEIGHT, ShapeType, COLOR

# turtle size default is 20x20
# setup window screen
wn = turtle.Screen()
wn.title("TETRIS BY Ryan Setaruddin")
wn.bgcolor("black")
wn.setup(width=600, height=800)
wn.tracer(0)

delay = 0.1

# Block class
class Block:
    """docstring for Block"""
    # constructor
    def __init__(self, x: int = 0, y: int = 0, color: str = COLOR, speed: int = 0):
        self.x, self.y = x, y
        self.color = color
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
    def __init__(self, x: int, y: int, shapeType: type):
        # Block Shape
        self.listOfBlocks = []
        self.color = COLOR
        self.shapeType = shapeType
        self.x, self.y = x, y
        self.speed = 5
        self.initiate_shape()

    # initiate shape method
    def initiate_shape(self):
        """ Create the list of blocks according to its shape type """
        if self.shapeType == ShapeType.I_TETROMINO:
            self.listOfBlocks.append(Block(self.x, self.y, self.color, self.speed+5))
            self.listOfBlocks.append(Block(self.x, self.y+BLOCK_HEIGHT, self.color, self.speed+5))
            self.listOfBlocks.append(Block(self.x, (self.y+BLOCK_HEIGHT*2), self.color, self.speed+5))
            self.listOfBlocks.append(Block(self.x, (self.y+BLOCK_HEIGHT*3), self.color, self.speed+5))
            self.listOfBlocks.append(Block(self.x, (self.y+BLOCK_HEIGHT*4), self.color, self.speed+5))

        elif self.shapeType == ShapeType.O_TETROMINO:
            self.listOfBlocks.append(Block(self.x, self.y, self.color, self.speed+10))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT, self.y, self.color, self.speed+10))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT, self.y-BLOCK_HEIGHT, self.color, self.speed+10))
            self.listOfBlocks.append(Block(self.x, self.y-BLOCK_HEIGHT, self.color, self.speed+10))

        elif self.shapeType == ShapeType.T_TETROMINO:
            self.listOfBlocks.append(Block(self.x, self.y, self.color, self.speed+5))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT, self.y, self.color, self.speed+5))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT*2, self.y, self.color, self.speed+5))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT, self.y+BLOCK_HEIGHT, self.color, self.speed+5))

        elif self.shapeType == ShapeType.L_TETROMINO:
            self.listOfBlocks.append(Block(self.x, self.y, self.color, self.speed+5))
            self.listOfBlocks.append(Block(self.x, self.y-BLOCK_HEIGHT, self.color, self.speed+5))
            self.listOfBlocks.append(Block(self.x, self.y-BLOCK_HEIGHT*2, self.color, self.speed+5))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT, self.y-BLOCK_HEIGHT*2, self.color, self.speed+5))

        elif self.shapeType == ShapeType.J_TETROMINO:
            self.listOfBlocks.append(Block(self.x, self.y, self.color, self.speed+5))
            self.listOfBlocks.append(Block(self.x, self.y-BLOCK_HEIGHT, self.color, self.speed+5))
            self.listOfBlocks.append(Block(self.x, self.y-BLOCK_HEIGHT*2, self.color, self.speed+5))
            self.listOfBlocks.append(Block(self.x-BLOCK_HEIGHT, self.y-BLOCK_HEIGHT*2, self.color, self.speed+5))

        elif self.shapeType == ShapeType.S_TETROMINO:
            self.listOfBlocks.append(Block(self.x, self.y, self.color, self.speed+5))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT, self.y, self.color, self.speed+5))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT, self.y+BLOCK_HEIGHT, self.color, self.speed+5))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT*2, self.y+BLOCK_HEIGHT, self.color, self.speed+5))

        elif self.shapeType == ShapeType.Z_TETROMINO:
            self.listOfBlocks.append(Block(self.x, self.y, self.color, self.speed+5))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT, self.y, self.color, self.speed+5))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT, self.y-BLOCK_HEIGHT, self.color, self.speed+5))
            self.listOfBlocks.append(Block(self.x+BLOCK_HEIGHT*2, self.y-BLOCK_HEIGHT, self.color, self.speed+5))

    # draw method
    def draw(self, pen):  
        # Go through the shape's blocks and draw them.
        for block in self.listOfBlocks:
            block.draw(pen)

# Tertis class
class Tetris:
    """docstring for Tetris"""
    # constructor
    def __init__(self, upcomingShapeState: list[Shape], fallingShapeState: list[Shape], existingShapeState: list[Shape], score: int = 0):
        self.upcomingShapeState = upcomingShapeState
        self.fallingShapeState = fallingShapeState
        self.existingShapeState = existingShapeState
        self.score = score
        self.pen = turtle.Turtle()

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
