
# Lagde en ekstra fil for å gjøre endringene i character class i task 3
# Kankje enklere å spille inn video om vi har de ulike filene? Kan se til slutt hvordan vi gjør det med filene

# Imports the Weapon class 
from items import Weapon

class Character:
    """Represents a character in the RPG"""

    def __init__(self, 
                 name: str, 
                 hp_max: int = 100, 
                 damage: int = 10,
                 weapon: Weapon | None = None 
                 ) -> None:
        """
        Initialise the Character 

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            weapon (Weapon | None): The weapon of the character, if it has has one.
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max # Burde denne også være en private attribute?
        self.damage = damage
        self.weapon = weapon

# Jeg har endret denne og lagt til weapon
    # Uses composition, a character can have a Weapon object
    # The Weapon object has a Dice object to determine damage
    def attack(self, target) -> None:
        """Attack and deal damage to target character"""

        # Check if the character has a weapon, if it has, use the weapon's damage dice
        if self.weapon is not None:
            damage = self.weapon.roll_damage()

       # Use the character's default damage if the character does not have a weapon
        else:
            damage = self.damage

        # Call the take_damage method on the target character to apply damage
        target.take_damage(damage)


    def take_damage(self, damage: int) -> None: 
        """Reduce the characters HP when taking damage"""
        self._hp -= damage
        self._hp = max(self._hp, 0) # Character hp cannot end up lower than 0


    def heal(self, amount) -> None:
        """Restore HP"""
        self._hp += amount
        self._hp = min(self._hp, self._hp_max) # Character cannot heal more than max hp
                                # Chat mente at vi burde bruke self.hp_max, ettersom det er det vi har som attributt 
    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp


    @property
    def is_alive(self) -> bool:
        """Return True if character is alive, False otherwise."""
        return self._hp > 0