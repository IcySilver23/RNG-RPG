from player import Player
from items import roll_for_loot
from events import generate_world_event
from black_market import BlackMarket
from relics import Relic
from weather import change_weather
from ai_npc import AI_NPC
from battle_pass import BattlePass, battle_pass_rewards
import random

def roll(player):
    """Roll for loot and add it to the player's inventory."""
    item = roll_for_loot()
    player.add_to_inventory(item)
    print(f"You received: {item}")

def main():
    name = input("Enter your player's name: ")
    class_type = input("Choose your class (Assassin, Mage, Berserker): ")
    player = Player(name, class_type)
    players = [player]  # Example list of players
    black_market = BlackMarket()  # Initialize Black Market
    npc = AI_NPC("John", "friendly", ["greet", "trade", "quest"])  # Example NPC
    battle_pass = BattlePass(season=1, levels=20, rewards=battle_pass_rewards)  # Initialize Battle Pass

    while True:
        print("\n1. Roll for loot")
        print("2. Show inventory")
        print("3. Equip item")
        print("4. Unequip item")
        print("5. Enhance item")
        print("6. Reforge item")
        print("7. Allocate stat points")
        print("8. Trigger world event")
        print("9. Access Black Market")
        print("10. List rare items in Black Market")
        print("11. Trade item")
        print("12. Add relic")
        print("13. Use relic")
        print("14. Choose profession")
        print("15. Level up profession")
        print("16. Craft item")
        print("17. Change weather")
        print("18. Interact with NPC")
        print("19. Check NPC behavior based on reputation")
        print("20. Show Battle Pass rewards")
        print("21. Gain Battle Pass level")
        print("22. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            roll(player)
        elif choice == '2':
            player.inventory.show_inventory()
        elif choice == '3':
            item_name = input("Enter the name of the item to equip: ")
            item = next((item for item in player.inventory.items if item.name == item_name), None)
            if item:
                player.equip_item(item)
            else:
                print("Item not found in inventory.")
        elif choice == '4':
            item_type = input("Enter the type of item to unequip (Weapon, Armor, Ring, Bracelet, Necklace): ")
            player.unequip_item(item_type)
        elif choice == '5':
            item_name = input("Enter the name of the item to enhance: ")
            item = next((item for item in player.inventory.items if item.name == item_name), None)
            if item:
                player.inventory.enhance_item(item)
            else:
                print("Item not found in inventory.")
        elif choice == '6':
            item_name = input("Enter the name of the item to reforge: ")
            item = next((item for item in player.inventory.items if item.name == item_name), None)
            if item:
                player.inventory.reforge_item(item)
            else:
                print("Item not found in inventory.")
        elif choice == '7':
            stat = input("Enter the stat to allocate points to (STR, AGI, INT): ")
            points = int(input("Enter the number of points to allocate: "))
            player.allocate_stat_points(stat, points)
        elif choice == '8':
            generate_world_event(players)
        elif choice == '9':
            black_market.display_items()
            item_index = int(input("Enter the index of the item to buy: ")) - 1
            black_market.buy_item(player, item_index)
        elif choice == '10':
            black_market.show_items()
        elif choice == '11':
            seller_name = input("Enter the name of the seller: ")
            buyer_name = input("Enter the name of the buyer: ")
            item_name = input("Enter the name of the item to trade: ")
            seller = next((p for p in players if p.name == seller_name), None)
            buyer = next((p for p in players if p.name == buyer_name), None)
            item = next((i for i in seller.inventory.items if i.name == item_name), None)
            if seller and buyer and item:
                player.trade_item(seller, buyer, item)
            else:
                print("Invalid trade details.")
        elif choice == '12':
            relic_name = input("Enter the name of the relic: ")
            effect = input("Enter the effect of the relic: ")
            cooldown = int(input("Enter the cooldown of the relic in seconds: "))
            relic = Relic(relic_name, effect, cooldown)
            player.add_relic(relic)
        elif choice == '13':
            relic_name = input("Enter the name of the relic to use: ")
            player.use_relic(relic_name)
        elif choice == '14':
            profession_name = input("Enter the profession to choose (Blacksmith, Alchemist, Enchanter): ")
            player.choose_profession(profession_name)
        elif choice == '15':
            player.level_up_profession()
        elif choice == '16':
            player.craft_item()
        elif choice == '17':
            current_weather = change_weather()
            current_weather.apply_effect(player)
        elif choice == '18':
            interaction_type = input("Enter the interaction type (greet, trade, quest): ")
            npc.interact(player, interaction_type)
        elif choice == '19':
            player_reputation = int(input("Enter the player's reputation: "))
            print(npc.interact_with_player(player_reputation))
        elif choice == '20':
            battle_pass.show_rewards()
        elif choice == '21':
            battle_pass.gain_level(player)
        elif choice == '22':
            print("Exiting game.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
