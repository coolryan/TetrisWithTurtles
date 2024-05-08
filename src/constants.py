"""
    Filename: constants.py.py
    Author: Ryan Setaruddin
    purpose: constnats
    Date: May 01, 2024
"""

# import library
from enum import Enum

COLOR = (
    "red", "blue", "purple", "lightblue", 
    "yellow", "orange", "green", "pink", "grey"
)

BLOCK_HEIGHT = 50

# ShapeType class
class ShapeType(Enum):
    I_TETROMINO = "I_TETROMINO"
    O_TETROMINO = "O_TETROMINO"
    T_TETROMINO = "T_TETROMINO"
    L_TETROMINO = "L_TETROMINO"
    J_TETROMINO = "J_TETROMINO"
    S_TETROMINO = "S_TETROMINO"
    Z_TETROMINO = "Z_TETROMINO"