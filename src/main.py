"""
    Filename: main.py
    Author: Ryan Setaruddin
    Purpose: To execute the program
    Date: Feb, 19, 2024
"""
# import library
import turtle

# import py files
from constants import BLOCK_HEIGHT, ShapeType
from tetris_model import Shape, Tetris

# main method
def main():
    # def __init__(self, upcomingShapeState: list[Shape], fallingShapeState: list[Shape], existingShapeState: list[Shape], score: int = 0):
    # def __init__(self, x: int, y: int, shapeType: type):
    fallingShapeState = [Shape(10, 10, ShapeType.I_TETROMINO)]
    upcomingShapeState = []
    existingShapeState = []
    tetris = Tetris(upcomingShapeState, fallingShapeState, existingShapeState, 0)
    tetris.draw()

# execuate the main program    
if __name__ == '__main__':
    main()
    turtle.exitonclick()