import random

class WorldEvent:
    def __init__(self):
        """Initialize world event with a type and description."""
        self.event_type, self.description = self.generate_event()

    def generate_event(self):
        """Generate a random world event."""
        events = [
            ("Invasion", "A horde of enemies is invading the land!"),
            ("Hidden Boss", "A powerful hidden boss has appeared!"),
            ("Festival", "A grand festival is being held, boosting morale!"),
            ("Meteor Shower", "A meteor shower is occurring, causing chaos!")
        ]
        return random.choice(events)

    def trigger_event(self, players):
        """Trigger the world event and allow all players to participate."""
        print(f"World Event: {self.event_type}")
        print(f"Description: {self.description}")
        for player in players:
            if self.event_type == "Invasion":
                self.handle_invasion(player)
            elif self.event_type == "Hidden Boss":
                self.handle_hidden_boss(player)
            elif self.event_type == "Festival":
                self.handle_festival(player)
            elif self.event_type == "Meteor Shower":
                self.handle_meteor_shower(player)

    def handle_invasion(self, player):
        """Handle invasion event for a player."""
        print(f"{player.name} is defending against the invasion!")
        # Example logic for invasion event
        player.gain_exp(50)
        player.gain_gold(100)

    def handle_hidden_boss(self, player):
        """Handle hidden boss event for a player."""
        print(f"{player.name} is fighting the hidden boss!")
        # Example logic for hidden boss event
        player.gain_exp(200)
        player.gain_gold(300)

    def handle_festival(self, player):
        """Handle festival event for a player."""
        print(f"{player.name} is enjoying the festival!")
        # Example logic for festival event
        player.restore_mana()
        player.gain_gold(50)

    def handle_meteor_shower(self, player):
        """Handle meteor shower event for a player."""
        print(f"{player.name} is surviving the meteor shower!")
        # Example logic for meteor shower event
        player.gain_exp(75)
        player.gain_gold(150)

def generate_world_event(players):
    """Generate and trigger a random world event."""
    event = WorldEvent()
    event.trigger_event(players)
