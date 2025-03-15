import random
from datetime import datetime, timedelta

class Quest:
    def __init__(self, name, objective, reward, time_limit=None):
        """Initialize a quest with objectives, rewards, and optional time limits."""
        self.name = name
        self.objective = objective
        self.reward = reward
        self.time_limit = time_limit
        self.start_time = datetime.now()

    def is_completed(self, player):
        """Check if the quest is completed by the player."""
        # Example logic for checking quest completion
        if self.objective == "Defeat Enemies":
            return player.enemies_defeated >= 10
        elif self.objective == "Collect Items":
            return player.items_collected >= 5
        elif self.objective == "Clear Dungeon":
            return player.dungeons_cleared >= 1
        return False

    def is_expired(self):
        """Check if the quest has expired based on the time limit."""
        if self.time_limit:
            return datetime.now() > self.start_time + timedelta(hours=self.time_limit)
        return False

    def reward_player(self, player):
        """Reward the player for completing the quest."""
        if self.is_completed(player):
            player.gain_gold(self.reward["gold"])
            player.gain_exp(self.reward["exp"])
            print(f"{player.name} completed the quest: {self.name}!")
            print(f"Rewards: {self.reward['gold']} gold, {self.reward['exp']} experience points.")
        else:
            print(f"{player.name} has not completed the quest: {self.name}.")

class QuestSystem:
    def __init__(self):
        """Initialize the quest system with a list of available quests."""
        self.available_quests = self.generate_quests()

    def generate_quests(self):
        """Generate a list of random quests."""
        quests = [
            Quest("Defeat 10 Enemies", "Defeat Enemies", {"gold": 100, "exp": 200}, time_limit=24),
            Quest("Collect 5 Rare Items", "Collect Items", {"gold": 150, "exp": 250}, time_limit=48),
            Quest("Clear the Dungeon", "Clear Dungeon", {"gold": 200, "exp": 300}),
            Quest("Gather 20 Herbs", "Collect Items", {"gold": 80, "exp": 150}, time_limit=24),
            Quest("Defeat the Goblin King", "Defeat Enemies", {"gold": 300, "exp": 400}),
            Quest("Craft a Legendary Item", "Craft Item", {"gold": 500, "exp": 600}),
            Quest("Trade with 3 NPCs", "Trade Items", {"gold": 120, "exp": 180}, time_limit=24)
        ]
        return quests

    def assign_quest(self, player):
        """Assign a random quest to the player."""
        quest = random.choice(self.available_quests)
        player.current_quest = quest
        print(f"{player.name} has been assigned the quest: {quest.name}")

    def check_quest_status(self, player):
        """Check the status of the player's current quest."""
        if player.current_quest:
            if player.current_quest.is_expired():
                print(f"The quest {player.current_quest.name} has expired.")
                player.current_quest = None
            elif player.current_quest.is_completed(player):
                player.current_quest.reward_player(player)
                player.current_quest = None
            else:
                print(f"{player.name} has not yet completed the quest: {player.current_quest.name}")
        else:
            print(f"{player.name} has no active quest.")
