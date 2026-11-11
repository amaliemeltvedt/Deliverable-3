from character_class_4 import Character


class Battle:
    """Manages a turn-based combat between two character objects"""

    def __init__(self,
                hero: Character,
                enemy: Character
                )-> None:
        """
        Initialise the Battle
        
        Args:
            hero (Character): The character created by the player
            enemy (Character): The opponent in the battle
        """
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """Play one round of combat between the hero and the enemy"""

        self.hero.attack(self.enemy)

        # The enemy only attacks if it is still alive
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        """Simulate the battle until one character is no longer alive"""

        # Loop continues as long as both are alive
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()

        # Loop stops when is_alive returns False for a Character
        # The Character that returns True then wins the battle
        if self.hero.is_alive:
            print(f"{self.hero.name} has won the battle!")

        else:
            print(f"{self.enemy.name} has won the battle!")