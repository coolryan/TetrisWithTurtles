"""
    Filename: main.py
    Author: Ryan Setaruddin
    Purpose: To execute the program
    Date: Feb, 19, 2024
"""
import turtle
from tetris_model import Shape

def main():
    # Create shape
    # Draw Shape
    block = Shape(x = 5, y = 5, color = "black", speed = 10)
    block.block_draw()
    
if __name__ == '__main__':
    main()
    turtle.exitonclick()