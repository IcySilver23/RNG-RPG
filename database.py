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
        "stat_points": player.stat_points,
        "inventory": [{"name": item.name, "item_type": item.item_type, "rarity": item.rarity, "stat_boost": item.stat_boost, "description": item.description, "cursed": item.cursed, "curse_penalty": item.curse_penalty} for item in player.inventory.items],
        "equipped_gear": {slot: ({"name": item.name, "item_type": item.item_type, "rarity": item.rarity, "stat_boost": item.stat_boost, "description": item.description, "cursed": item.cursed, "curse_penalty": item.curse_penalty} if item else None) for slot, item in player.equipped_gear.items()},
        "class_type": player.class_type,
        "stats": player.stats,
        "skills": [{"name": skill.name, "mana_cost": skill.mana_cost, "damage_multiplier": skill.damage_multiplier, "scaling_stat": skill.scaling_stat} for skill in player.skills],
        "currency": player.currency,
        "titles": [{"name": title.name, "buff": title.buff} for title in player.titles],
        "relics": [{"name": relic.name, "effect": relic.effect, "cooldown": relic.cooldown} for relic in player.relics],
        "profession": {"name": player.profession.name, "skill_level": player.profession.skill_level, "bonuses": player.profession.bonuses} if player.profession else None
    }
    with open(filename, "w") as file:
        json.dump(player_data, file, indent=4)
    print(f"Game saved to {filename}")

def load_game(filename="savegame.json"):
    """Load the player's game state from a JSON file."""
    with open(filename, "r") as file:
        player_data = json.load(file)
    
    player = Player(player_data["name"], player_data["class_type"])
    player.level = player_data["level"]
    player.exp = player_data["exp"]
    player.stat_points = player_data["stat_points"]
    player.inventory.items = [Item(**item) for item in player_data["inventory"]]
    player.equipped_gear = {slot: (Item(**item) if item else None) for slot, item in player_data["equipped_gear"].items()}
    player.stats = player_data["stats"]
    player.skills = [Skill(**skill) for skill in player_data["skills"]]
    player.currency = player_data["currency"]
    player.titles = [Title(**title) for title in player_data["titles"]]
    player.relics = [Relic(**relic) for relic in player_data["relics"]]
    if player_data["profession"]:
        player.profession = Profession(**player_data["profession"])
    
    print(f"Game loaded from {filename}")
    return player

