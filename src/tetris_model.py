"""
    Filename: tetris_model.py
    Author: Ryan Setaruddin
    purpose: To create a class called Tetris and base class called Block
    This will represents the game
    Date: Feb, 19, 2024
"""
import turtle

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
    def draw(self):
        pass

class Tetris:
    """docstring for Tetris"""
    def __init__(self, upcomingBlockstate: list[Block], fallingBlockState: list{Block}, existingBlockState: list{Block}, score: int = 0):
        self.upcomingBlockstate = upcomingBlockstate
        self.fallingBlockState = fallingBlockState
        self.existingBlockState = existingBlockState
        self.score = score

    def draw(self):
        pass
