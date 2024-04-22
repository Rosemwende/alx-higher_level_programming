#!/usr/bin/python3
"""write the class Rectangle that inherits from Base"""

from models.base import Base

class Rectangle(Base):
    """Rectangle class inheriting from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
