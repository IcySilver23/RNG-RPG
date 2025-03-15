class Profession:
    def __init__(self, name, skill_level, bonuses):
        """Initialize a profession with skill levels and crafting bonuses."""
        self.name = name
        self.skill_level = skill_level
        self.bonuses = bonuses
        self.recipes = self.generate_recipes()

    def generate_recipes(self):
        """Generate a list of recipes based on profession and skill level."""
        recipes = []
        if self.name == "Blacksmith":
            recipes = ["Iron Sword", "Steel Armor"] if self.skill_level >= 1 else []
            if self.skill_level >= 5:
                recipes.append("Dragon Slayer Sword")
        elif self.name == "Alchemist":
            recipes = ["Healing Potion", "Mana Potion"] if self.skill_level >= 1 else []
            if self.skill_level >= 5:
                recipes.append("Elixir of Immortality")
        elif self.name == "Enchanter":
            recipes = ["Fire Enchantment", "Ice Enchantment"] if self.skill_level >= 1 else []
            if self.skill_level >= 5:
                recipes.append("Legendary Enchantment")
        return recipes

    def level_up(self):
        """Level up the profession and unlock new recipes."""
        self.skill_level += 1
        self.recipes = self.generate_recipes()
        print(f"{self.name} leveled up to skill level {self.skill_level}! New recipes unlocked: {self.recipes}")

# Example professions
professions = [
    Profession("Blacksmith", 1, "Crafts powerful weapons & armor"),
    Profession("Alchemist", 1, "Creates potions with unique effects"),
    Profession("Enchanter", 1, "Imbues gear with magical properties")
]
