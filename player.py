from skill import Skill
from titles import TitleSystem
from inventory import Inventory
from items import available_sets
from secret_classes import check_unlock_conditions
from relics import Relic
from professions import Profession
import random

class Player:
    def __init__(self, name, class_type):
        """Initialize player with base stats and inventory."""
        self.name = name
        self.level = 1
        self.exp = 0
        self.stat_points = 0  # Initialize stat points
        self.inventory = Inventory()  # Initialize inventory
        self.equipped_gear = {"Weapon": None, "Armor": None, "Ring": None, "Bracelet": None, "Necklace": None}  # Initialize equipped gear
        self.class_type = class_type
        self.stats = self.initialize_stats(class_type)
        self.skills = self.initialize_skills()
        self.currency = 0  # Initialize currency
        self.titles = []  # Initialize titles
        self.title_system = TitleSystem()  # Initialize title system
        self.hp = 100  # Initialize HP
        self.mana = self.stats['INT'] * 10  # Initialize mana
        self.enemies_defeated = 0  # Track enemies defeated
        self.items_stolen = 0  # Track items stolen
        self.relics = []  # Initialize relics
        self.profession = None  # Initialize profession

    def initialize_stats(self, class_type):
        """Initialize stats based on class type."""
        if class_type == 'Assassin':
            return {'STR': 5, 'AGI': 10, 'INT': 3, 'DEF': 5}
        elif class_type == 'Mage':
            return {'STR': 3, 'AGI': 5, 'INT': 10, 'DEF': 3}
        elif class_type == 'Berserker':
            return {'STR': 10, 'AGI': 5, 'INT': 3, 'DEF': 7}
        else:
            raise ValueError("Invalid class type")

    def initialize_skills(self):
        """Initialize unique skills based on class type."""
        if self.class_type == 'Assassin':
            return [Skill('Backstab', 10, 1.5, 'AGI'), Skill('Shadow Strike', 15, 2.0, 'AGI')]
        elif self.class_type == 'Mage':
            return [Skill('Fireball', 10, 1.5, 'INT'), Skill('Ice Blast', 15, 2.0, 'INT')]
        elif self.class_type == 'Berserker':
            return [Skill('Power Smash', 10, 1.5, 'STR'), Skill('Rage', 15, 2.0, 'STR')]
        else:
            raise ValueError("Invalid class type")

    def level_up(self):
        """Level up the player, increase stats, and restore mana."""
        self.level += 1
        self.exp = 0
        self.stat_points += 5  # Example: 5 stat points per level
        self.restore_mana()
        print(f"{self.name} leveled up to level {self.level}! You have {self.stat_points} stat points to allocate.")

    def allocate_stat_points(self, stat, points):
        """Allocate stat points to a specific stat."""
        if points <= self.stat_points:
            self.stats[stat] += points
            self.stat_points -= points
            print(f"{points} points allocated to {stat}. New {stat}: {self.stats[stat]}")
        else:
            print("Not enough stat points.")

    def restore_mana(self):
        """Restore player's mana to full."""
        self.mana = self.stats['INT'] * 10

    def gain_exp(self, amount):
        """Gain experience and level up if enough experience is gained."""
        self.exp += amount
        if self.exp >= 100:
            self.level_up()
        check_unlock_conditions(self)  # Check for secret class unlocks

    def add_to_inventory(self, item):
        """Add an item to the player's inventory and apply stat boost."""
        self.inventory.add_item(item)

    def equip_item(self, item):
        """Equip an item from the inventory."""
        self.inventory.equip_item(item)
        if item.item_type in self.equipped_gear:
            self.equipped_gear[item.item_type] = item
            for stat, boost in item.stat_boost.items():
                self.stats[stat] += boost
            print(f"{item.name} equipped. Stats boosted: {item.stat_boost}")
            self.check_set_bonus()

    def unequip_item(self, item_type):
        """Unequip an item and return it to the inventory, removing stat boosts."""
        if item_type in self.equipped_gear and self.equipped_gear[item_type]:
            item = self.equipped_gear[item_type]
            self.equipped_gear[item_type] = None
            self.inventory.add_item(item)
            for stat, boost in item.stat_boost.items():
                self.stats[stat] -= boost
            print(f"{item.name} unequipped. Stats reduced: {item.stat_boost}")

    def check_set_bonus(self):
        """If a player equips all required set pieces, activate the set bonus."""
        equipped_names = {item.name for item in self.equipped_gear.values() if item}
        for item_set in available_sets:
            if all(req in equipped_names for req in item_set.required_items):
                print(f"Set Bonus Activated: {item_set.name} (+{item_set.bonus_amount} {item_set.bonus_stat})")
                self.apply_stat_bonus(item_set.bonus_stat, item_set.bonus_amount)

    def apply_stat_bonus(self, stat, amount):
        """Apply a stat bonus to the player."""
        if stat in self.stats:
            self.stats[stat] += amount
            print(f"{stat} increased by {amount}. New {stat}: {self.stats[stat]}")

    def choose_class(self, chosen_class):
        """Choose a class and boost the corresponding stat."""
        self.class_type = chosen_class
        if chosen_class == 'Assassin':
            self.stats['AGI'] += 5
        elif chosen_class == 'Mage':
            self.stats['INT'] += 5
        elif chosen_class == 'Berserker':
            self.stats['STR'] += 5
        else:
            raise ValueError("Invalid class type")

    def take_damage(self, damage):
        """Reduce HP by damage amount and check if HP reaches zero."""
        dodge_chance = self.stats['AGI'] * 0.01  # Example: 1% dodge chance per AGI point
        if random.random() < dodge_chance:
            print(f"{self.name} dodged the attack!")
            return False  # Player dodged the attack
        damage_taken = max(0, damage - self.stats['DEF'])
        self.hp -= damage_taken
        if self.hp <= 0:
            self.hp = 0
            return True  # Player is defeated
        return False  # Player is still alive

    def use_skill(self, skill, enemy):
        """Use a skill on an enemy, costing mana and dealing damage."""
        if self.mana >= skill.mana_cost:
            self.mana -= skill.mana_cost
            damage = self.stats[skill.scaling_stat] * skill.damage_multiplier
            enemy.take_damage(damage)
            print(f"{self.name} used {skill.name} on {enemy.name} for {damage} damage!")
        else:
            print(f"Not enough mana to use {skill.name}.")

    def awaken_secret_class(self):
        """Unlock hidden classes like Monarch or Shadow Lord."""
        hidden_classes = {
            'Monarch': {'STR': 15, 'AGI': 15, 'INT': 15, 'DEF': 10},
            'Shadow Lord': {'STR': 20, 'AGI': 10, 'INT': 20, 'DEF': 5}
        }
        if self.level >= 10 and any(item.rarity == 'Legendary' for item in self.inventory.items):
            chosen_class = random.choice(list(hidden_classes.keys()))
            self.class_type = chosen_class
            self.stats.update(hidden_classes[chosen_class])
            print(f"{self.name} has awakened as a {chosen_class}!")
            print(f"New stats: {self.stats}")
        else:
            print("Conditions not met for awakening a secret class.")

    def gain_gold(self, amount):
        """Gain gold."""
        self.currency += amount
        print(f"{self.name} gained {amount} gold. Total gold: {self.currency}")

    def earn_title(self, title_name):
        """Earn a title based on achievements."""
        self.title_system.award_title(self, title_name)

    def trade_item(self, seller, buyer, item):
        """Trade an item from the seller to the buyer."""
        if item in seller.inventory.items:
            seller.inventory.remove_item(item)
            buyer.inventory.add_item(item)
            print(f"{seller.name} traded {item.name} to {buyer.name}.")
        else:
            print(f"{item.name} not found in {seller.name}'s inventory.")

    def defeat_enemy(self):
        """Increment the count of defeated enemies."""
        self.enemies_defeated += 1

    def steal_item(self):
        """Increment the count of stolen items."""
        self.items_stolen += 1

    def unlock_secret_class(self, secret_class):
        """Unlock a secret class for the player."""
        self.class_type = secret_class.name
        self.skills.append(Skill(secret_class.unique_skill, 0, 0, 'STR'))  # Example skill addition
        print(f"{self.name} has unlocked the secret class: {secret_class.name}!")
        print(f"New skill acquired: {secret_class.unique_skill}")

    def add_relic(self, relic):
        """Add a relic to the player's collection."""
        self.relics.append(relic)
        print(f"{relic.name} added to relics.")

    def use_relic(self, relic_name):
        """Use a relic by name."""
        relic = next((r for r in self.relics if r.name == relic_name), None)
        if relic:
            relic.use_relic(self)
        else:
            print(f"Relic {relic_name} not found.")

    def choose_profession(self, profession_name):
        """Choose a profession for the player."""
        if profession_name == "Blacksmith":
            self.profession = Profession("Blacksmith", 1, "Crafts powerful weapons & armor")
        elif profession_name == "Alchemist":
            self.profession = Profession("Alchemist", 1, "Creates potions with unique effects")
        elif profession_name == "Enchanter":
            self.profession = Profession("Enchanter", 1, "Imbues gear with magical properties")
        else:
            print("Invalid profession.")
            return
        print(f"{self.name} has chosen the profession: {self.profession.name}")

    def level_up_profession(self):
        """Level up the player's profession."""
        if self.profession:
            self.profession.level_up()
        else:
            print("No profession chosen.")

    def craft_item(self):
        """Craft an item based on the player's profession."""
        if self.profession:
            if self.profession.name == "Blacksmith":
                crafted_item = random.choice(["Iron Sword", "Steel Armor", "Dragon Slayer Sword"])
            elif self.profession.name == "Alchemist":
                crafted_item = random.choice(["Healing Potion", "Mana Potion", "Elixir of Immortality"])
            elif self.profession.name == "Enchanter":
                crafted_item = random.choice(["Fire Enchantment", "Ice Enchantment", "Legendary Enchantment"])
            else:
                print("Invalid profession.")
                return
            print(f"{self.name} crafted a {crafted_item}!")
        else:
            print("No profession chosen.")

