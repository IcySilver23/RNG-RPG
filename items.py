import random

class Item:
    def __init__(self, name, item_type, rarity, stat_boost, description, cursed=False, curse_penalty=0):
        """Initialize item with name, item type, rarity, stat boost, description, and optional curse effects."""
        self.name = name
        self.item_type = item_type
        self.rarity = rarity
        self.stat_boost = stat_boost
        self.description = description
        self.cursed = cursed
        self.curse_penalty = curse_penalty

    def __repr__(self):
        return f"Item(name={self.name}, item_type={self.item_type}, rarity={self.rarity}, stat_boost={self.stat_boost}, description={self.description}, cursed={self.cursed}, curse_penalty={self.curse_penalty})"

class ItemSet:
    def __init__(self, name, required_items, bonus_stat, bonus_amount):
        """Initialize item set with name, required items, bonus stat, and bonus amount."""
        self.name = name
        self.required_items = required_items
        self.bonus_stat = bonus_stat
        self.bonus_amount = bonus_amount

    def __repr__(self):
        return f"ItemSet(name={self.name}, required_items={self.required_items}, bonus_stat={self.bonus_stat}, bonus_amount={self.bonus_amount})"

# Example item sets
available_sets = [
    ItemSet("Dragon Set", ["Dragon Sword", "Dragon Armor"], "STR", 10),
    ItemSet("Phoenix Set", ["Phoenix Armor", "Phoenix Shield"], "AGI", 10)
]

def roll_for_loot():
    """Roll for loot, where higher rarity is rarer."""
    items = [
        {"name": "Wooden Sword", "rarity": "Common", "stat_boost": {"STR": 2}, "description": "A basic wooden sword.", "item_type": "Weapon"},
        {"name": "Leather Armor", "rarity": "Common", "stat_boost": {"AGI": 3}, "description": "Basic leather armor.", "item_type": "Armor"},
        {"name": "Iron Ring", "rarity": "Common", "stat_boost": {"INT": 1}, "description": "A simple iron ring.", "item_type": "Accessory"},
        {"name": "Steel Sword", "rarity": "Uncommon", "stat_boost": {"STR": 5}, "description": "A sturdy steel sword.", "item_type": "Weapon"},
        {"name": "Chainmail Armor", "rarity": "Uncommon", "stat_boost": {"AGI": 6}, "description": "Protective chainmail armor.", "item_type": "Armor"},
        {"name": "Silver Ring", "rarity": "Uncommon", "stat_boost": {"INT": 4}, "description": "A shiny silver ring.", "item_type": "Accessory"},
        {"name": "Magic Sword", "rarity": "Rare", "stat_boost": {"STR": 8}, "description": "A sword imbued with magic.", "item_type": "Weapon"},
        {"name": "Plate Armor", "rarity": "Rare", "stat_boost": {"AGI": 9}, "description": "Heavy plate armor.", "item_type": "Armor"},
        {"name": "Gold Ring", "rarity": "Rare", "stat_boost": {"INT": 7}, "description": "A valuable gold ring.", "item_type": "Accessory"},
        {"name": "Dragon Sword", "rarity": "Epic", "stat_boost": {"STR": 12}, "description": "A sword made from dragon scales.", "item_type": "Weapon"},
        {"name": "Dragon Armor", "rarity": "Epic", "stat_boost": {"AGI": 13}, "description": "Armor made from dragon scales.", "item_type": "Armor"},
        {"name": "Platinum Ring", "rarity": "Epic", "stat_boost": {"INT": 11}, "description": "A rare platinum ring.", "item_type": "Accessory"},
        {"name": "Excalibur", "rarity": "Legendary", "stat_boost": {"STR": 20}, "description": "The legendary sword Excalibur.", "item_type": "Weapon"},
        {"name": "Phoenix Armor", "rarity": "Legendary", "stat_boost": {"AGI": 18}, "description": "Armor with the power of the phoenix.", "item_type": "Armor"},
        {"name": "Diamond Ring", "rarity": "Legendary", "stat_boost": {"INT": 15}, "description": "A ring with a large diamond.", "item_type": "Accessory"},
        {"name": "Emerald Amulet", "rarity": "Rare", "stat_boost": {"INT": 10}, "description": "An amulet with a large emerald.", "item_type": "Accessory"},
        {"name": "Ruby Dagger", "rarity": "Epic", "stat_boost": {"STR": 15}, "description": "A dagger with a ruby hilt.", "item_type": "Weapon"},
        {"name": "Sapphire Shield", "rarity": "Legendary", "stat_boost": {"DEF": 20}, "description": "A shield with a sapphire core.", "item_type": "Armor"},
        {"name": "Cursed Sword", "rarity": "Cursed", "stat_boost": {"STR": 25}, "description": "A powerful but cursed sword.", "item_type": "Weapon", "cursed": True, "curse_penalty": 5},
        {"name": "Cursed Armor", "rarity": "Cursed", "stat_boost": {"AGI": 20}, "description": "A powerful but cursed armor.", "item_type": "Armor", "cursed": True, "curse_penalty": 5},
        {"name": "Dagger of the Demon King", "rarity": "Legendary", "stat_boost": {"STR": 30}, "description": "A dagger once wielded by the Demon King.", "item_type": "Weapon"},
        {"name": "Cloak of Shadows", "rarity": "Epic", "stat_boost": {"AGI": 25}, "description": "A cloak that grants the wearer the power of shadows.", "item_type": "Armor"},
        {"name": "Ring of Eternal Flame", "rarity": "Legendary", "stat_boost": {"INT": 20}, "description": "A ring that burns with an eternal flame.", "item_type": "Accessory"},
        {"name": "Masamune", "rarity": "Legendary", "stat_boost": {"STR": 35}, "description": "The legendary katana wielded by Sephiroth.", "item_type": "Weapon"},
        {"name": "Genji Armor", "rarity": "Legendary", "stat_boost": {"DEF": 25}, "description": "Armor worn by the legendary warrior Gilgamesh.", "item_type": "Armor"},
        {"name": "Ribbon", "rarity": "Epic", "stat_boost": {"INT": 15}, "description": "A ribbon that protects against all status ailments.", "item_type": "Accessory"},
        {"name": "Thunder Hammer", "rarity": "Epic", "stat_boost": {"STR": 18}, "description": "A hammer that crackles with thunder.", "item_type": "Weapon"},
        {"name": "Mystic Robe", "rarity": "Rare", "stat_boost": {"INT": 12}, "description": "A robe that enhances magical abilities.", "item_type": "Armor"},
        {"name": "Guardian Shield", "rarity": "Epic", "stat_boost": {"DEF": 22}, "description": "A shield that provides immense protection.", "item_type": "Armor"},
        {"name": "Warrior's Helm", "rarity": "Uncommon", "stat_boost": {"STR": 7}, "description": "A helm worn by seasoned warriors.", "item_type": "Armor"},
        {"name": "Sorcerer's Staff", "rarity": "Epic", "stat_boost": {"INT": 17}, "description": "A staff that channels powerful spells.", "item_type": "Weapon"},
        {"name": "Boots of Speed", "rarity": "Rare", "stat_boost": {"AGI": 14}, "description": "Boots that increase the wearer's speed.", "item_type": "Armor"},
        {"name": "Ring of Wisdom", "rarity": "Legendary", "stat_boost": {"INT": 25}, "description": "A ring that grants immense wisdom.", "item_type": "Accessory"},
        {"name": "Dragon Claw", "rarity": "Epic", "stat_boost": {"STR": 20}, "description": "A claw from a mighty dragon.", "item_type": "Weapon"},
        {"name": "Elven Bow", "rarity": "Rare", "stat_boost": {"AGI": 12}, "description": "A bow crafted by elves.", "item_type": "Weapon"},
        {"name": "Titan's Gauntlets", "rarity": "Legendary", "stat_boost": {"STR": 30}, "description": "Gauntlets that grant the strength of a titan.", "item_type": "Armor"},
        {"name": "Shadow Blade", "rarity": "Epic", "stat_boost": {"STR": 22}, "description": "A blade that strikes from the shadows.", "item_type": "Weapon"},
        {"name": "Holy Shield", "rarity": "Legendary", "stat_boost": {"DEF": 28}, "description": "A shield blessed with holy power.", "item_type": "Armor"},
        {"name": "Arcane Tome", "rarity": "Epic", "stat_boost": {"INT": 19}, "description": "A tome filled with arcane knowledge.", "item_type": "Accessory"},
        {"name": "Vampire Cloak", "rarity": "Legendary", "stat_boost": {"AGI": 26}, "description": "A cloak that grants the agility of a vampire.", "item_type": "Armor"},
        {"name": "Storm Bringer", "rarity": "Epic", "stat_boost": {"STR": 24}, "description": "A weapon that brings the storm.", "item_type": "Weapon"},
        {"name": "Nature's Blessing", "rarity": "Legendary", "stat_boost": {"INT": 27}, "description": "An amulet blessed by nature.", "item_type": "Accessory"}
    ]
    item = random.choice(items)
    return Item(name=item["name"], item_type=item["item_type"], rarity=item["rarity"], stat_boost=item["stat_boost"], description=item["description"], cursed=item.get("cursed", False), curse_penalty=item.get("curse_penalty", 0))
