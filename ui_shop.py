from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QLabel
from shop import Shop

class ShopUI:
    def __init__(self, player):
        self.player = player
        self.shop = Shop()
        self.shop_panel = QVBoxLayout()
        self.update_shop_panel()

    def update_shop_panel(self):
        """Update the shop panel with items for sale."""
        self.shop_panel.addWidget(QLabel("Shop:"))
        for index, item in enumerate(self.shop.items_for_sale):
            item_button = QPushButton(f"{item.name} (Cost: {item.stat_boost * 10} gold)", self)
            item_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.5); color: cyan; border: 1px solid cyan;")
            item_button.clicked.connect(lambda _, i=index: self.buy_item(i))
            self.shop_panel.addWidget(item_button)

    def buy_item(self, item_index):
        """Buy an item from the shop."""
        self.shop.buy_item(self.player, item_index)
        self.update_shop_panel()
