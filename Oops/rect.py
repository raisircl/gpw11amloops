class Rect:
    '''A class representing a rectangle with width and height.'''
    count=0 # Class Attribute to keep track of the number of Rect instances
    def __init__(self, len=1, wid=1):
        """Initialize a new rectangle with default dimensions."""
        print("Rect Constructor called")
        self.length = len  # Instance Attribute
        self.width = wid # Instance Attribute
        Rect.count += 1  # Increment the count of Rect instances
        self.id=Rect.count  # Assign a unique ID to the rectangle instance

    def display(self):
        """Display the dimensions of the rectangle."""
        print(f"Rect{self.id} Dimension: {self.length}x{self.width}")
    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width
    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.length + self.width)    