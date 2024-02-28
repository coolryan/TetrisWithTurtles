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
    def draw(self):
        pen = turtle.Turtle()

        pen.shape("square")
        pen.speed(self.speed)
        pen.penup()

        pen.color(self.color)
        colors = ["green", "red", "lightblue", "blue", "yellow", "orange", "purple"]

        for b in range(5):
            pen.color(colors[b])
            screen_x, screen_y = self.x, self.y
            pen.goto(screen_x, screen_y+b*25)
            pen.stamp()

class Tetris:
    """docstring for Tetris"""
    def __init__(self, upcomingBlockstate: list[Block], fallingBlockState: list[Block], existingBlockState: list[Block], score: int = 0):
        self.upcomingBlockstate = upcomingBlockstate
        self.fallingBlockState = fallingBlockState
        self.existingBlockState = existingBlockState
        self.score = score


#wn.mainloop()
