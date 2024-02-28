"""
    Filename: main.py
    Author: Ryan Setaruddin
    Purpose: To execute the program
    Date: Feb, 19, 2024
"""
import turtle
from tetris_model import Shape

def main():
    block = Shape(x = 30, y = 30, color = "green", speed = 10)
    block.draw()
    
if __name__ == '__main__':
    main()
    turtle.exitonclick()