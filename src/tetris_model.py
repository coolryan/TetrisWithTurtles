"""
    Filename: tetris_model.py
    Author: Ryan Setaruddin
    purpose: To design a game called Tetris
    by each of classes that may need help with such a base class called
    Block where it takes 4 paramters in constructor and one draw method
    in which can not draw its self

    Another base class called IBlock which is drived from Block class
    must have draw method which takes 4 paramters

    another base class called Tetris which takes 4 paramters in its constructors
    and one draw method
    This will represents the game
    Date: Feb, 19, 2024
"""
import turtle
import time
import random

class Block:
    """docstring for Block"""
    def __init__(self, x: int, y: int, color: str, speed: int = 0):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed

    def draw(self):
        raise NotImplementedError

class IBlock(Block):
    """docstring for I_Block"""
    def draw(self, x: int, y: int, color: str, speed: int):
        wall = []
        for i in range(2):
            block = turtle.Turtle()
            block.shape("square")
            block.color("color")
            block.penup()
            wall.append(block)
        wall[0].goto(x, y)
        wall.stamp()
        wall[1].goto(x, y)
        wall.stamp()

        return wall

class Tetris:
    """docstring for Tetris"""
    def __init__(self, upcomingBlockstate: list[Block], fallingBlockState: list{Block}, existingBlockState: list{Block}, score: int = 0):
        self.upcomingBlockstate = upcomingBlockstate
        self.fallingBlockState = fallingBlockState
        self.existingBlockState = existingBlockState
        self.score = score

    def draw(self):
        pass

iblock = IBlock(20, 20 "lightblue", 1)