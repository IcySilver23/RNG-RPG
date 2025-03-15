class Title:
    def __init__(self, name, buff):
        """Initialize title with name and buff."""
        self.name = name
        self.buff = buff

    def __repr__(self):
        return f"Title(name={self.name}, buff={self.buff})"

class TitleSystem:
    def __init__(self):
        """Initialize title system with a list of possible titles."""
        self.titles = self.generate_titles()

    def generate_titles(self):
        """Generate a list of possible titles and their buffs."""
        return [
            Title("Dragon Slayer", {"STR": 5}),
            Title("Master Mage", {"INT": 5}),
            Title("Shadow Assassin", {"AGI": 5}),
            Title("Dungeon Conqueror", {"STR": 3, "AGI": 3, "INT": 3}),
            Title("Wealthy Merchant", {"currency": 100})
        ]

    def award_title(self, player, title_name):
        """Award a title to a player based on achievements."""
        for title in self.titles:
            if title.name == title_name:
                player.titles.append(title)
                for stat, boost in title.buff.items():
                    if stat in player.stats:
                        player.stats[stat] += boost
                    elif stat == "currency":
                        player.currency += boost
                print(f"{player.name} earned the title: {title.name}!")
                print(f"New stats: {player.stats}")
                return
        print(f"Title {title_name} not found.")

    def apply_title(self, player, title_name):
        """Apply the effect of a title to a player."""
        for title in player.titles:
            if title.name == title_name:
                for stat, boost in title.buff.items():
                    if stat in player.stats:
                        player.stats[stat] += boost
                    elif stat == "currency":
                        player.currency += boost
                print(f"{player.name} applied the title: {title.name}!")
                print(f"New stats: {player.stats}")
                return
        print(f"Title {title_name} not found in player's titles.")
