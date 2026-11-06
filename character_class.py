# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

# Endringer: fjernet alt fra attack metoden og lagde ny metode kalt take_damage i stedet
# Nå vil attack gjøre at target mister hp (liv) uten å endre _hp
# La også til en heal() metode som legger til x antall hp til karakteren
# Lagde en is_alive property som returnerer en boolsk verdi (true/false) avhengig av om hp er over/under 0
# Har ikke dobbeltsjekket dette med chatgpt så mulig noe er feil

class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage

# Denne er endret
    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        target.take_damage(self.damage)

# Denne er ny
    def take_damage(self, damage: int) -> None: 
        """Reduce the characters HP when taking damage"""
        self._hp -= damage
        self._hp = max(self._hp, 0) # Character hp cannot end up lower than 0

# Denne er ny
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
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

# Denne er ny
    @property
    def is_alive(self) -> bool:
        """Return True if character is alive, False otherwise."""
        return self._hp > 0