class Relic:
    def __init__(self, name, effect, cooldown):
        """Initialize a relic with special abilities and cooldowns."""
        self.name = name
        self.effect = effect
        self.cooldown = cooldown
        self.last_used = None

    def use_relic(self, player):
        """Use the relic's effect if it's not on cooldown."""
        from datetime import datetime, timedelta
        if self.last_used is None or datetime.now() >= self.last_used + timedelta(seconds=self.cooldown):
            self.apply_effect(player)
            self.last_used = datetime.now()
            print(f"{self.name} used! Effect: {self.effect}")
        else:
            remaining_cooldown = (self.last_used + timedelta(seconds=self.cooldown) - datetime.now()).seconds
            print(f"{self.name} is on cooldown. Try again in {remaining_cooldown} seconds.")

    def apply_effect(self, player):
        """Apply the relic's effect to the player."""
        # Example effect logic
        if self.effect == "Heal":
            player.hp = min(player.hp + 50, 100)
            print(f"{player.name} healed for 50 HP. Current HP: {player.hp}")
        elif self.effect == "Mana Boost":
            player.mana = min(player.mana + 30, player.stats['INT'] * 10)
            print(f"{player.name} gained 30 mana. Current mana: {player.mana}")

# Example relics
legendary_relics = [
    Relic("Timeworn Hourglass", "Rewinds time 10 seconds", 3600),  # 1 hour cooldown
    Relic("Demon King's Heart", "Boosts all stats by 50% at low HP", 0)  # Passive
]
