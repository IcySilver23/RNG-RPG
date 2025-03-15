class SecretClass:
    def __init__(self, name, unlock_requirement, unique_skill):
        """Initialize a secret class with unlock conditions and special abilities."""
        self.name = name
        self.unlock_requirement = unlock_requirement
        self.unique_skill = unique_skill

    def __repr__(self):
        return f"SecretClass(name={self.name}, unlock_requirement={self.unlock_requirement}, unique_skill={self.unique_skill})"

# Example secret classes
secret_classes = [
    SecretClass("Shadow Monarch", "Defeat 100 enemies alone", "Summon Shadow Army"),
    SecretClass("Arcane Trickster", "Steal 50 items", "Illusion Clone")
]

def check_unlock_conditions(player):
    """Check if the player meets the conditions to unlock any secret classes."""
    for secret_class in secret_classes:
        if secret_class.unlock_requirement == "Defeat 100 enemies alone" and player.enemies_defeated >= 100:
            player.unlock_secret_class(secret_class)
        elif secret_class.unlock_requirement == "Steal 50 items" and player.items_stolen >= 50:
            player.unlock_secret_class(secret_class)