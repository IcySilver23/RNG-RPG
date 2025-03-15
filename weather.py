class Weather:
    def __init__(self, type, effect):
        """Initialize weather conditions with specific gameplay effects."""
        self.type = type
        self.effect = effect

    def apply_effect(self, player):
        """Apply the weather effect to the player."""
        if self.effect == "Lightning strikes randomly in battles":
            # Example effect logic
            print(f"{player.name} is struck by lightning!")
            player.take_damage(10)
        elif self.effect == "Reduces movement speed by 50%":
            # Example effect logic
            print(f"{player.name}'s movement speed is reduced by 50%!")
        elif self.effect == "Reduces accuracy in ranged combat":
            # Example effect logic
            print(f"{player.name}'s accuracy in ranged combat is reduced!")

    def spawn_boss(self):
        """Spawn a boss if the weather condition is met."""
        if self.type == "Thunderstorm":
            print("The Thunder Dragon appears!")
        elif self.type == "Blizzard":
            print("The Ice Golem appears!")
        elif self.type == "Fog":
            print("The Shadow Assassin appears!")

# Example weather effects
weather_types = [
    Weather("Thunderstorm", "Lightning strikes randomly in battles"),
    Weather("Blizzard", "Reduces movement speed by 50%"),
    Weather("Fog", "Reduces accuracy in ranged combat")
]

def change_weather():
    """Change the weather to a random type."""
    import random
    current_weather = random.choice(weather_types)
    print(f"The weather has changed to: {current_weather.type}")
    current_weather.spawn_boss()
    return current_weather
