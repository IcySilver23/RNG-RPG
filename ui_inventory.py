from PyQt6.QtWidgets import QGridLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from player import Player

class InventoryUI:
    def __init__(self, player):
        self.player = player
        self.inventory_grid = QGridLayout()
        self.update_inventory_grid()

    def update_inventory_grid(self):
        """Update the inventory grid with the current items."""
        for i in reversed(range(self.inventory_grid.count())):
            self.inventory_grid.itemAt(i).widget().setParent(None)

        rarity_colors = {
            "Common": "white",
            "Rare": "blue",
            "Epic": "purple",
            "Legendary": "gold"
        }
        row, col = 0, 0
        for item in self.player.inventory.items:
            item_button = QPushButton(item.name)
            item_button.setStyleSheet(f"border: 2px solid {rarity_colors.get(item.rarity, 'white')}; color: white; background-color: rgba(0, 0, 0, 0.5);")
            item_button.clicked.connect(lambda _, i=item: self.equip_item(i))
            self.inventory_grid.addWidget(item_button, row, col)
            col += 1
            if col > 4:
                col = 0
                row += 1

    def equip_item(self, item):
        """Equip an item and update the UI."""
        self.player.equip_item(item)
        self.update_inventory_grid()
        self.update_equipment_section()

    def update_equipment_section(self):
        """Update the equipment section with the currently equipped items."""
        for i in reversed(range(self.equipment_section.count())):
            self.equipment_section.itemAt(i).widget().setParent(None)

        rarity_colors = {
            "Common": "white",
            "Uncommon": "green",
            "Rare": "blue",
            "Epic": "purple",
            "Legendary": "gold"
        }
        for slot, item in self.player.equipped_gear.items():
            item_label = QLabel(f"{slot}: {item.name if item else 'None'}")
            item_label.setStyleSheet(f"border: 2px solid {rarity_colors.get(item.rarity if item else 'Common', 'white')}; color: white; background-color: rgba(0, 0, 0, 0.5);")
            self.equipment_section.addWidget(item_label)
