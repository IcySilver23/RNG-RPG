class Skill:
    def __init__(self, name, mana_cost, damage_multiplier, scaling_stat):
        """Initialize skill with name, mana cost, damage multiplier, and scaling stat."""
        self.name = name
        self.mana_cost = mana_cost
        self.damage_multiplier = damage_multiplier
        self.scaling_stat = scaling_stat

    def __repr__(self):
        return f"Skill(name={self.name}, mana_cost={self.mana_cost}, damage_multiplier={self.damage_multiplier}, scaling_stat={self.scaling_stat})"

    def use_skill(self, player, target):
        """Cast a skill, reducing mana and dealing damage."""
        if player.mana >= self.mana_cost:
            player.mana -= self.mana_cost
            damage = player.stats[self.scaling_stat] * self.damage_multiplier
            target.take_damage(damage)
            print(f"{player.name} used {self.name} on {target.name} for {damage} damage!")
        else:
            print(f"Not enough mana to use {self.name}.")
