from enemies import Enemy, enemies, bosses
from items import roll_for_loot
import random

class Dungeon:
    def __init__(self, name, difficulty):
        """Initialize a dungeon with a name, difficulty, enemy list, and loot rewards."""
        self.name = name
        self.difficulty = difficulty
        self.enemies = self.generate_enemies()
        self.rewards = self.generate_rewards()

    def generate_enemies(self):
        """Generate a list of random enemies based on difficulty."""
        num_enemies = {
            'easy': random.randint(1, 3),
            'medium': random.randint(2, 4),
            'hard': random.randint(3, 5)
        }.get(self.difficulty, 2)
        
        level_modifier = {
            'easy': -1,
            'medium': 0,
            'hard': 1
        }.get(self.difficulty, 0)
        
        return [random.choice(enemies) for _ in range(num_enemies)]

    def generate_rewards(self):
        """Generate a list of random loot rewards."""
        return [roll_for_loot() for _ in range(random.randint(1, 3))]

    def enter(self, player):
        """Player enters the dungeon, fights enemies, and earns rewards."""
        print(f"{player.name} enters the {self.name} dungeon!")
        for enemy in self.enemies:
            print(f"A wild {enemy.name} appears!")
            while enemy.hp > 0 and player.hp > 0:
                # Player attacks enemy
                damage = player.stats['STR']
                if enemy.take_damage(damage):
                    print(f"{enemy.name} is defeated!")
                    break
                # Enemy attacks player
                damage = enemy.attack_power
                if player.take_damage(damage):
                    print(f"{player.name} is defeated!")
                    return
            print(f"{player.name} defeated {enemy.name}!")
            player.gain_exp(50)  # Example experience gain
        print(f"{player.name} cleared the {self.name} dungeon!")
        self.reward_player(player)

    def start_dungeon(self, player):
        """Start the dungeon run, where the player fights until all enemies are defeated."""
        print(f"{player.name} is starting the {self.name} dungeon!")
        for enemy in self.enemies:
            print(f"A wild {enemy.name} appears!")
            while enemy.hp > 0 and player.hp > 0:
                # Player attacks enemy
                damage = player.stats['STR']
                if enemy.take_damage(damage):
                    print(f"{enemy.name} is defeated!")
                    break
                # Enemy attacks player
                damage = enemy.attack_power
                if player.take_damage(damage):
                    print(f"{player.name} is defeated!")
                    return
            print(f"{player.name} defeated {enemy.name}!")
            player.gain_exp(50)  # Example experience gain
        print(f"{player.name} cleared the {self.name} dungeon!")
        self.reward_player(player)

    def reward_player(self, player):
        """Reward player with loot and XP after clearing the dungeon."""
        bonus_exp = 100  # Example bonus experience
        player.gain_exp(bonus_exp)
        print(f"{player.name} gained {bonus_exp} bonus experience!")
        for loot in self.rewards:
            player.add_to_inventory(loot)
            print(f"{player.name} received loot: {loot.name}!")
        bonus_gold = random.randint(50, 100)  # Example gold reward range
        player.gain_gold(bonus_gold)

# Example dungeons
dungeons = [
    Dungeon("Goblin Cave", "easy"),
    Dungeon("Haunted Forest", "medium"),
    Dungeon("Dragon's Lair", "hard"),
    Dungeon("Crystal Cavern", "medium"),
    Dungeon("Ancient Ruins", "hard"),
    Dungeon("Volcanic Depths", "hard"),
    Dungeon("Frozen Tundra", "medium"),
    Dungeon("Shadow Realm", "hard")
]
