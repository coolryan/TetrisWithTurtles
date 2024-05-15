"""
    Filename: main.py
    Author: Ryan Setaruddin
    Purpose: To execute the program
    Date: Feb, 19, 2024
"""
# import library
import turtle

# import py files
from constants import BLOCK_HEIGHT, ShapeType, COLOR
from tetris_model import Shape, Tetris

# main method
def main():
    # def __init__(self, upcomingShapeState: list[Shape], fallingShapeState: list[Shape], existingShapeState: list[Shape], score: int = 0):
    # def __init__(self, x: int, y: int, shapeType: type):
    fallingShapeState = [
        Shape(-100, 0, ShapeType.I_TETROMINO, COLOR.LIGHTBLUE), 
        Shape(0, 100, ShapeType.O_TETROMINO),
        Shape(200, 100, ShapeType.T_TETROMINO),
        Shape(-280, 100, ShapeType.L_TETROMINO),
        Shape(-200, -200, ShapeType.J_TETROMINO),
        Shape(400, 100, ShapeType.S_TETROMINO),
        Shape(400, -100, ShapeType.Z_TETROMINO, COLOR.GREY)
    ]
    upcomingShapeState = []
    existingShapeState = []
    tetris = Tetris(upcomingShapeState, fallingShapeState, existingShapeState, 0)
    tetris.start_game()

# execuate the main program    
if __name__ == '__main__':
    main()
    turtle.exitonclick()

turtle.mainloop()
