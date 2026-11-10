from character_class_4 import Character

class Battle:
    """Manages a turn based combat between two charachter objects"""

    def __init__(self, hero: Character, enemy: Character) -> None:
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """Play one round of combat between the hero and the enemy"""

        self.hero.attack(self.enemy)

        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        """Simulate the battle until one character is no longer alive"""
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()

        if self.hero.is_alive:
            print(f"{self.hero.name} has won the battle!")

        else:
            print(f"{self.enemy.name} has won the battle!")