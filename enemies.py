class Enemy:
    def __init__(self, name, level):
        """Initialize enemy with name, level, HP, and attack power."""
        self.name = name
        self.level = level
        self.hp = self.calculate_hp(level)
        self.attack_power = self.calculate_attack_power(level)

    def calculate_hp(self, level):
        """Calculate HP based on level."""
        return 50 + (level * 10)

    def calculate_attack_power(self, level):
        """Calculate attack power based on level."""
        return 5 + (level * 2)

    def take_damage(self, damage):
        """Reduce HP by damage amount and check if HP reaches zero."""
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            return True  # Enemy is defeated
        return False  # Enemy is still alive

# Example enemies
enemies = [
    Enemy("Goblin", 1),
    Enemy("Skeleton", 2),
    Enemy("Orc", 3),
    Enemy("Dark Knight", 5),
    Enemy("Fire Elemental", 7),
    Enemy("Ice Elemental", 7),
    Enemy("Shadow Assassin", 10),
    Enemy("Vampire", 12),
    Enemy("Necromancer", 15),
    Enemy("Dragon", 20)
]

# Example bosses
bosses = [
    Enemy("Goblin King", 10),
    Enemy("Lich King", 15),
    Enemy("Demon Lord", 20),
    Enemy("Ancient Dragon", 25),
    Enemy("Titan", 30)
]
