from items import Item
import random

class BlackMarket:
    def __init__(self):
        """Initialize a secret shop with unique loot."""
        self.items_for_sale = self.generate_items()

    def generate_items(self):
        """Generate a list of rare, cursed, and illegal items for sale."""
        items = [
            Item(name="Cursed Sword", item_type="Weapon", rarity="Cursed", stat_boost={"STR": 25}, description="A powerful but cursed sword.", cursed=True, curse_penalty=5),
            Item(name="Cursed Armor", item_type="Armor", rarity="Cursed", stat_boost={"AGI": 20}, description="A powerful but cursed armor.", cursed=True, curse_penalty=5),
            Item(name="Shadow Dagger", item_type="Weapon", rarity="Epic", stat_boost={"STR": 15}, description="A dagger that grants the power of shadows."),
            Item(name="Ring of Deception", item_type="Accessory", rarity="Legendary", stat_boost={"INT": 20}, description="A ring that hides the wearer's true intentions."),
            Item(name="Boots of Swiftness", item_type="Armor", rarity="Epic", stat_boost={"AGI": 25}, description="Boots that increase the wearer's speed."),
            Item(name="Amulet of the Fallen", item_type="Accessory", rarity="Legendary", stat_boost={"DEF": 30}, description="An amulet that protects the wearer from harm."),
            Item(name="Demon King's Crown", item_type="Accessory", rarity="Legendary", stat_boost={"INT": 35}, description="A crown that grants immense magical power."),
            Item(name="Vampire's Fang", item_type="Weapon", rarity="Epic", stat_boost={"STR": 20}, description="A fang that drains the life of enemies."),
            Item(name="Necromancer's Robe", item_type="Armor", rarity="Legendary", stat_boost={"INT": 25}, description="A robe that enhances dark magic."),
            Item(name="Assassin's Cloak", item_type="Armor", rarity="Epic", stat_boost={"AGI": 20}, description="A cloak that grants stealth and agility.")
        ]
        return random.sample(items, 3)  # Example: 3 items for sale

    def display_items(self):
        """Display items available for sale."""
        for index, item in enumerate(self.items_for_sale):
            print(f"{index + 1}. {item.name} (Rarity: {item.rarity}, Stat Boost: {item.stat_boost}, Description: {item.description})")

    def buy_item(self, player, item_index):
        """Allow player to buy an item if they have enough currency."""
        if 0 <= item_index < len(self.items_for_sale):
            item = self.items_for_sale[item_index]
            item_cost = item.stat_boost["STR"] * 20  # Example cost calculation
            if player.currency >= item_cost:
                player.currency -= item_cost
                player.add_to_inventory(item)
                print(f"{player.name} bought {item.name} for {item_cost} gold!")
            else:
                print("Not enough currency to buy this item.")
        else:
            print("Invalid item index.")

    def show_items(self):
        """List rare items available in the Black Market."""
        rare_items = [item for item in self.items_for_sale if item.rarity in ["Epic", "Legendary", "Cursed"]]
        if rare_items:
            print("Rare items available in the Black Market:")
            for item in rare_items:
                print(f"- {item.name} (Rarity: {item.rarity}, Stat Boost: {item.stat_boost}, Description: {item.description})")
        else:
            print("No rare items available in the Black Market.")
