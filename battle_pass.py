from items import Item

class BattlePass:
    def __init__(self, season, levels, rewards):
        """Initialize a battle pass with seasonal rewards."""
        self.season = season
        self.levels = levels
        self.rewards = rewards
        self.current_level = 0

    def gain_level(self, player):
        """Increase the player's battle pass level and unlock rewards."""
        if self.current_level < self.levels:
            self.current_level += 1
            reward = self.rewards.get(self.current_level)
            if reward:
                self.apply_reward(player, reward)
                print(f"Battle Pass Level {self.current_level} reached! Reward unlocked: {reward}")
            else:
                print(f"Battle Pass Level {self.current_level} reached!")
        else:
            print("Battle Pass is already at max level.")

    def apply_reward(self, player, reward):
        """Apply the reward to the player."""
        if reward == "Exclusive Sword Skin":
            player.add_to_inventory(Item("Exclusive Sword", "Weapon", "Epic", {"STR": 15}, "A sword with an exclusive skin."))
        elif reward == "XP Boost Potion":
            player.gain_exp(500)
        elif reward == "Legendary Armor Set":
            player.add_to_inventory(Item("Legendary Armor", "Armor", "Legendary", {"DEF": 30}, "A set of legendary armor."))
        elif reward == "Epic Mount":
            player.add_to_inventory(Item("Epic Mount", "Mount", "Epic", {"AGI": 20}, "An epic mount that increases speed."))
        elif reward == "Mythic Weapon":
            player.add_to_inventory(Item("Mythic Weapon", "Weapon", "Mythic", {"STR": 40}, "A weapon of mythic power."))
        elif reward == "Gold":
            player.gain_gold(1000)
        elif reward == "Mana Potion":
            player.mana = min(player.mana + 50, player.stats['INT'] * 10)
        elif reward == "Health Potion":
            player.hp = min(player.hp + 50, 100)
        elif reward == "Skill Point":
            player.stat_points += 1

    def show_rewards(self):
        """Display the rewards for each level of the battle pass."""
        print(f"Battle Pass Season {self.season} Rewards:")
        for level in range(1, self.levels + 1):
            reward = self.rewards.get(level, "No reward")
            print(f"Level {level}: {reward}")

# Example rewards per level.
battle_pass_rewards = {
    1: "Exclusive Sword Skin",
    2: "Gold",
    3: "Mana Potion",
    4: "Health Potion",
    5: "XP Boost Potion",
    6: "Gold",
    7: "Skill Point",
    8: "Mana Potion",
    9: "Health Potion",
    10: "Legendary Armor Set",
    11: "Gold",
    12: "Mana Potion",
    13: "Health Potion",
    14: "Skill Point",
    15: "Epic Mount",
    16: "Gold",
    17: "Mana Potion",
    18: "Health Potion",
    19: "Skill Point",
    20: "Mythic Weapon"
}

# Example Battle Pass
battle_pass = BattlePass(season=1, levels=20, rewards=battle_pass_rewards)
