
import random

# Creates a Dice class that can create a dice with a specified number of sides 
class Dice:
    """Represents a dice with n sides"""

    def __init__(self, sides: int = 6) -> None:
        """
        Initialise a dice object.
        
        Args:
            sides (int): Number of sides on the dice (default = 6).
                         Must be at least 2.
        """
        # Checks if the dice has at least 2 sides, raises an error if not
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides.")
        
        # Stores the number of sides as an attribute of the object
        self.sides = sides

    # Creates a method to roll the dice 
    def roll(self) -> int:
        """
        Roll the dice and return a random number.

        Returns:
            int: A random integer between 1 and the number of sides.
        """
        return random.randint(1, self.sides)

    # Defines how a Dice object is represented when printed
    def __repr__(self) -> str:
        """
        Return a string representation of the dice object.

        Returns:
            str: A string showing the number of sides on the dice.
        """
        return f"Dice(sides={self.sides})"

    # This special method makes it possible to use the Dice object as a function
    def __call__(self) -> int:
        """
        Allow the dice object to be called like a function.
        
        Returns:
            int: The result of rolling the dice.
        """
        return self.roll() 
