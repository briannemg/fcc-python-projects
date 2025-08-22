"""
polygon_shapes.py

A module for working with rectangles and squares using object-oriented programming.
"""

from __future__ import annotations  # for forward type hints (Python <3.11)

class Rectangle:
    """
    A class representing a rectangle.
    """

    def __init__(self, width: int, height: int) -> None:
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, width: int) -> None:
        self.width = width

    def set_height(self, height: int) -> None:
        self.height = height

    def get_area(self) -> int:
        """Return the area of the rectangle."""
        return self.width * self.height
    
    def get_perimeter(self) -> int:
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
    
    def get_diagonal(self) -> float:
        """Return the length of the diagonal."""
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self) -> str:
        """Return a string representation of the rectangle using '*'."""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height
    
    def get_amount_inside(self, other: Rectangle) -> int:
        """
        Return the number of times `other` rectangle can fit inside this rectangle.
        No rotation is considered.
        """
        times_width = self.width // other.width
        times_height = self.height // other.height
        return times_width * times_height
    
class Square(Rectangle):
    """
    A class representing a square, subclass of Rectangle.
    """

    def __init__(self, side: int) -> None:
        super().__init__(side, side)

    def __str__(self) -> str:
        return f"Square(side={self.width})"
    
    def set_side(self, side: int) -> None:
        """Set the side of the square (updates both width and height)."""
        self.width = side
        self.height = side

    def set_width(self, width: int) -> None:
        self.set_side(width)

    def set_height(self, height: int) -> None:
        self.set_side(height)


# Example usage (only runs when executed directly)
if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(f"Area: {rect.get_area()}")
    rect.set_height(3)
    print(f"Perimeter: {rect.get_perimeter()}")
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(f"Area: {sq.get_area()}")
    sq.set_side(4)
    print(f"Diagonal: {sq.get_diagonal():.2f}")
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(f"Number of squares inside rectangle: {rect.get_amount_inside(sq)}")