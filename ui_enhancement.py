from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QInputDialog
from player import Player
import random

class EnhancementUI:
    def __init__(self, player):
        self.player = player
        self.enhancement_panel = QVBoxLayout()
        self.update_enhancement_panel()

    def update_enhancement_panel(self):
        """Update the enhancement panel with reforge and upgrade options."""
        self.enhancement_panel.addWidget(QLabel("Enhance Your Gear:"))

        # Reforge Table
        self.reforge_table = QTableWidget(5, 2)
        self.reforge_table.setHorizontalHeaderLabels(["Item", "Reforge"])
        self.update_reforge_table()
        self.enhancement_panel.addWidget(self.reforge_table)

        # Upgrade Button
        self.upgrade_button = QPushButton("Upgrade Item", self)
        self.upgrade_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.5); color: cyan; border: 1px solid cyan;")
        self.upgrade_button.clicked.connect(self.upgrade_item)
        self.enhancement_panel.addWidget(self.upgrade_button)

    def update_reforge_table(self):
        """Update the reforge table with the player's items."""
        self.reforge_table.setRowCount(len(self.player.inventory.items))
        for row, item in enumerate(self.player.inventory.items):
            item_name = QTableWidgetItem(item.name)
            reforge_button = QPushButton("Reforge", self)
            reforge_button.clicked.connect(lambda _, i=item: self.reforge_item(i))
            self.reforge_table.setItem(row, 0, item_name)
            self.reforge_table.setCellWidget(row, 1, reforge_button)

    def reforge_item(self, item):
        """Reforge an item and update the UI."""
        self.player.inventory.reforge_item(item)
        self.update_reforge_table()
        self.update_combat_log(f"{item.name} has been reforged!")

    def upgrade_item(self):
        """Upgrade an item with a chance of failure."""
        item_name, ok = QInputDialog.getText(self, "Upgrade Item", "Enter the name of the item to upgrade:")
        if ok:
            item = next((i for i in self.player.inventory.items if i.name == item_name), None)
            if item:
                success_rate = 80 - (item.stat_boost['STR'] // 2)  # Example success rate calculation
                if random.randint(1, 100) <= success_rate:
                    self.player.inventory.enhance_item(item)
                    self.update_reforge_table()
                    self.update_combat_log(f"{item.name} has been successfully upgraded!")
                else:
                    self.update_combat_log(f"Upgrade failed! {item.name} remains unchanged.")
            else:
                self.update_combat_log(f"Item {item_name} not found in inventory.")

    def update_combat_log(self, message):
        """Update the combat log with a new message."""
        self.combat_log.append(message)
