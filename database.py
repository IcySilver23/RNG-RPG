import json
from player import Player
from items import Item
from skill import Skill
from titles import Title

def save_game(player, filename="savegame.json"):
    """Save the player's game state to a JSON file."""
    player_data = {
        "name": player.name,
        "level": player.level,
        "exp": player.exp,
        "inventory": [{"name": item.name, "rarity": item.rarity, "stat_boost": item.stat_boost, "description": item.description} for item in player.inventory],
        "class_type": player.class_type,
        "stats": player.stats,
        "skills": [{"name": skill.name, "mana_cost": skill.mana_cost, "damage_multiplier": skill.damage_multiplier, "scaling_stat": skill.scaling_stat} for skill in player.skills],
        "currency": player.currency,
        "titles": [{"name": title.name, "buff": title.buff} for title in player.titles]
    }
    with open(filename, "w") as file:
        json.dump(player_data, file)
    print(f"Game saved to {filename}")

def load_game(filename="savegame.json"):
    """Load the player's game state from a JSON file."""
    with open(filename, "r") as file:
        player_data = json.load(file)
    
    player = Player(player_data["name"], player_data["class_type"])
    player.level = player_data["level"]
    player.exp = player_data["exp"]
    player.inventory = [Item(**item) for item in player_data["inventory"]]
    player.stats = player_data["stats"]
    player.skills = [Skill(**skill) for skill in player_data["skills"]]
    player.currency = player_data["currency"]
    player.titles = [Title(**title) for title in player_data["titles"]]
    
    print(f"Game loaded from {filename}")
    return player

