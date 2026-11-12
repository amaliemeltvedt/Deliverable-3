# Imports the Dice class from dice_class.py
from dice_class import Dice


# Defines a Weapon class using composition
# Each weapon contains a Dice object that can determine the weapon's damage
class Weapon:
    """Represents a weapon that deals damage using a dice."""

    def __init__(
            self, 
            name: str, 
            damage_dice: Dice
    ) -> None:
        """
        Initialise a weapon object.

        Args:
            name (str): Name of the weapon.
            damage_dice (Dice): The dice used to decide the weapon damage.
        """  
        self.name = name
        self.damage_dice = damage_dice

    # Creates a method to roll the weapon's damage dice
    def roll_damage(self) -> int:
        """
        Roll the weapon's damage dice and return the damage value.
        
        Returns:
            int: The damage dealt by the weapon.
        """
        # Uses the Dice object's roll() method to determine the damage 
        return self.damage_dice.roll() 