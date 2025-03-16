from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QLabel
from black_market import BlackMarket

class BlackMarketUI:
    def __init__(self, player):
        self.player = player
        self.black_market = BlackMarket()
        self.black_market_panel = QVBoxLayout()
        self.update_black_market_panel()

    def update_black_market_panel(self):
        """Update the Black Market panel with rare items for sale."""
        self.black_market_panel.addWidget(QLabel("Black Market:"))
        for index, item in enumerate(self.black_market.items_for_sale):
            item_button = QPushButton(f"{item.name} (Cost: {item.stat_boost['STR'] * 20} gold)", self)
            item_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.5); color: cyan; border: 1px solid cyan;")
            item_button.clicked.connect(lambda _, i=index: self.buy_item(i))
            self.black_market_panel.addWidget(item_button)

    def buy_item(self, item_index):
        """Buy an item from the Black Market."""
        self.black_market.buy_item(self.player, item_index)
        self.update_black_market_panel()
