import random

class Inventory:
    def __init__(self):
        """Initialize inventory with items and equipped gear."""
        self.items = []
        self.equipped_gear = {
            "Weapon": None,
            "Armor": None,
            "Ring": None,
            "Bracelet": None,
            "Necklace": None
        }
        self.stats = {
            "Strength": 0,
            "Defense": 0,
            "Agility": 0,
            "Intelligence": 0
        }

    def add_item(self, item):
        """Add an item to the inventory."""
        self.items.append(item)
        print(f"{item.name} added to inventory.")

    def remove_item(self, item):
        """Remove an item from the inventory."""
        if item in self.items:
            self.items.remove(item)
            print(f"Removed {item.name} from inventory.")
        else:
            print(f"{item.name} not found in inventory.")

    def equip_item(self, item):
        """Equip an item from the inventory and apply stat boosts."""
        if item in self.items:
            if item.item_type in ["Weapon", "Armor", "Ring", "Bracelet", "Necklace"]:
                self.equipped_gear[item.item_type] = item
                self.items.remove(item)
                for stat, boost in item.stat_boost.items():
                    self.stats[stat] += boost
                print(f"Equipped {item.name}. Stats boosted: {item.stat_boost}")
            else:
                print(f"{item.name} cannot be equipped.")
        else:
            print(f"{item.name} not found in inventory.")

    def unequip_item(self, item_type):
        """Unequip an item and return it to the inventory, removing stat boosts."""
        if item_type in self.equipped_gear and self.equipped_gear[item_type]:
            item = self.equipped_gear[item_type]
            self.equipped_gear[item_type] = None
            self.items.append(item)
            for stat, boost in item.stat_boost.items():
                self.stats[stat] -= boost
            print(f"Unequipped {item.name}. Stats reduced: {item.stat_boost}")
        else:
            print(f"No {item_type} equipped.")

    def show_inventory(self):
        """Display the contents of the inventory."""
        if not self.items:
            print("Inventory is empty.")
        else:
            print("Inventory contents:")
            for item in self.items:
                print(f"- {item.name} (Rarity: {item.rarity}, Stat Boost: {item.stat_boost}, Description: {item.description})")

    def enhance_item(self, item):
        """Increase the stat boost of an item with a chance of failure."""
        success_rate = 80  # % success chance
        if random.randint(1, 100) <= success_rate:
            for stat in item.stat_boost:
                item.stat_boost[stat] += 5  # Increase stat boost
            print(f"{item.name} has been successfully enhanced! (+5 to each stat)")
        else:
            print(f"Enhancement failed! {item.name} remains unchanged.")

    def reforge_item(self, item):
        """Reroll an item's stat boost within a certain range."""
        for stat in item.stat_boost:
            min_stat = item.stat_boost[stat] - 3
            max_stat = item.stat_boost[stat] + 5
            item.stat_boost[stat] = random.randint(min_stat, max_stat)
        print(f"{item.name} has been reforged! New stat boost: {item.stat_boost}")
