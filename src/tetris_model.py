"""
    Filename: tetris_model.py
    Author: Ryan Setaruddin
    purpose: To design a game called Tetris
    This will represents the game
    Date: Feb, 19, 2024
"""
from enum import Enum
import random
import time

import turtle

class ShapeType(Enum):
    I_TETROMINO = "I_TETROMINO"
    O_TETROMINO = "O_TETROMINO"
    T_TETROMINO = "T_TETROMINO"
    L_TETROMINO = "L_TETROMINO"
    J_TETROMINO = "J_TETROMINO"
    S_TETROMINO = "S_TETROMINO"
    Z_TETROMINO = "Z_TETROMINO"

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
        self.height = 0
        self.weight = 0

    # create the drawing pen
    pen = turtle.Turtle()

    def block_draw(self, pen):
        pen.penup()
        pen.speed(self.speed)
        pen.shape("square")
        pen.setundobuffer(None)

        pen.clear()
        top, left = self.x, self.y

        colors = ["black", "lightblue", "blue", "orange", "yellow", "green", "purple", "red"]

        for h in range(len(self.height)):
            for w in range(len(self.weigh)):
                screen_x, screen_y = left + (h * 20), top - (w * 20)
                color_number = [h][w]
                color = colors[color_number]
                pen.color(color)
                pen.goto(screen_x, screen_y)
                pen.stamp()

    # draw the score
    def draw_score(pen, score):
        pen.color("blue")
        pen.hideturtle()
        pen.goto(self.x, self.y)
        pen.write("Score: {}".format(score), move=False, align="left", font=("Arial", 24, "normal"))

class Shape:
    """docstring for Shape"""
    # to draw the Shape
    def __init__(self, listOfBlocks: list[Block], shapeType: Type):
        # Block Shape
        self.listOfBlocks = listOfBlocks
        self.shapeType = shapeType

    # create the drawing pen
    pen = turtle.Turtle()

    def shape_draw(self, pen):
        pen.up()
        pen.shape(shapeType)

class Tetris:
    """docstring for Tetris"""
    def __init__(self, upcomingShapeState: list[Shape], fallingShapeState: list[Shape], existingShapeState: list[Shape], score: int = 0):
        self.upcomingShapeState = upcomingShapeState
        self.fallingShapeState = fallingBlockState
        self.existingShapeState = existingShapeState
        self.score = score
    
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
