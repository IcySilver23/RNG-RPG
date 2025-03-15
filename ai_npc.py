class AI_NPC:
    def __init__(self, name, personality, behavior_patterns):
        """Initialize an NPC with different behaviors based on interactions."""
        self.name = name
        self.personality = personality
        self.behavior_patterns = behavior_patterns
        self.relationship_status = {}

    def interact(self, player, interaction_type):
        """Interact with the player and change behavior based on interaction type."""
        if interaction_type == "greet":
            self.greet(player)
        elif interaction_type == "trade":
            self.trade(player)
        elif interaction_type == "quest":
            self.give_quest(player)
        else:
            print(f"{self.name} does not understand the interaction.")

    def greet(self, player):
        """Greet the player based on personality."""
        if self.personality == "friendly":
            print(f"{self.name} warmly greets {player.name}.")
        elif self.personality == "hostile":
            print(f"{self.name} glares at {player.name}.")
        else:
            print(f"{self.name} nods at {player.name}.")

    def trade(self, player):
        """Trade items with the player."""
        print(f"{self.name} is ready to trade with {player.name}.")
        # Example trade logic
        item = player.inventory.items[0] if player.inventory.items else None
        if item:
            player.inventory.remove_item(item)
            print(f"{self.name} traded an item with {player.name}.")
        else:
            print(f"{self.name} has nothing to trade.")

    def give_quest(self, player):
        """Give a quest to the player."""
        print(f"{self.name} has a quest for {player.name}.")
        # Example quest logic
        quest = {"name": "Collect 10 Herbs", "reward": {"gold": 50, "exp": 100}}
        player.current_quest = quest
        print(f"{player.name} received a quest: {quest['name']}")

    def react_to_world_event(self, event_type):
        """React to world events."""
        if event_type == "Invasion":
            print(f"{self.name} is preparing for the invasion!")
        elif event_type == "Hidden Boss":
            print(f"{self.name} is scared of the hidden boss!")
        elif event_type == "Festival":
            print(f"{self.name} is excited about the festival!")
        elif event_type == "Meteor Shower":
            print(f"{self.name} is taking cover from the meteor shower!")

    def interact_with_player(self, player_reputation):
        """Interact with the player based on their reputation."""
        if player_reputation > 50:
            return f"{self.name} greets you warmly."
        elif player_reputation < -50:
            return f"{self.name} refuses to speak with you."
        else:
            return f"{self.name} is neutral towards you."
