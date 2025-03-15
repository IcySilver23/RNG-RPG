from items import Item
import random

class Shop:
    def __init__(self):
        """Initialize shop with a list of items for sale."""
        self.items_for_sale = self.generate_items()

    def generate_items(self):
        """Generate a list of random items for sale."""
        items = []
        item_types = ['Weapon', 'Armor', 'Potion']
        for _ in range(5):  # Example: 5 items for sale
            item_type = random.choice(item_types)
            rarity = random.choice(['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'])
            stat_boost = random.randint(1, 10)
            item = Item(name=f"{rarity} {item_type}", rarity=rarity, stat_boost=stat_boost, description=f"A {rarity.lower()} {item_type.lower()}.")
            items.append(item)
        return items

    def display_items(self):
        """Display items available for sale."""
        for index, item in enumerate(self.items_for_sale):
            print(f"{index + 1}. {item.name} (Rarity: {item.rarity}, Stat Boost: {item.stat_boost}, Description: {item.description})")

    def buy_item(self, player, item_index):
        """Allow player to buy an item if they have enough currency."""
        if 0 <= item_index < len(self.items_for_sale):
            item = self.items_for_sale[item_index]
            item_cost = item.stat_boost * 10  # Example cost calculation
            if player.currency >= item_cost:
                player.currency -= item_cost
                player.add_to_inventory(item)
                print(f"{player.name} bought {item.name} for {item_cost} gold!")
            else:
                print("Not enough currency to buy this item.")
        else:
            print("Invalid item index.")

    def sell_item(self, player, item_index):
        """Allow player to sell an item from their inventory."""
        if 0 <= item_index < len(player.inventory):
            item = player.inventory.pop(item_index)
            sell_price = item.stat_boost * 5  # Example sell price calculation
            player.currency += sell_price
            print(f"{player.name} sold {item.name} for {sell_price} gold!")
        else:
            print("Invalid item index.")
