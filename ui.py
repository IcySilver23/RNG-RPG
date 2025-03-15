from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QListWidget
from PyQt6.QtGui import QFont, QColor, QPalette
from PyQt6.QtCore import Qt
from items import roll_for_loot
from player import Player

class MainWindow(QMainWindow):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.setWindowTitle("Solo Leveling RNG")
        self.setGeometry(100, 100, 600, 400)
        self.set_dark_theme()

        # Title Label
        self.title_label = QLabel("Solo Leveling RNG", self)
        self.title_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        self.title_label.setStyleSheet("color: cyan; text-shadow: 0 0 10px cyan;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Player Stats Label
        self.stats_label = QLabel(self)
        self.update_stats_label()

        # Roll for Loot Button
        self.roll_button = QPushButton("Roll for Loot", self)
        self.roll_button.clicked.connect(self.roll_for_loot)

        # Inventory Panel
        self.inventory_list = QListWidget(self)
        self.inventory_list.setStyleSheet("""
            QListWidget {
                border: 2px solid cyan;
                border-radius: 5px;
                padding: 5px;
                background-color: #333;
                color: white;
            }
            QListWidget::item {
                padding: 5px;
            }
        """)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.stats_label)
        layout.addWidget(self.roll_button)
        layout.addWidget(self.inventory_list)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def set_dark_theme(self):
        """Set a dark theme for the application."""
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
        palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
        self.setPalette(palette)

    def roll_for_loot(self):
        """Roll for loot and update the player's inventory and stats."""
        item = roll_for_loot()
        self.player.add_to_inventory(item)
        self.update_stats_label()
        self.update_inventory_list()
        print(f"You received: {item}")

    def update_stats_label(self):
        """Update the player stats label with the current stats."""
        stats_text = f"Name: {self.player.name}\nLevel: {self.player.level}\nHP: {self.player.hp}\nMana: {self.player.mana}\nGold: {self.player.currency}"
        self.stats_label.setText(stats_text)

    def update_inventory_list(self):
        """Update the inventory list with the current items."""
        self.inventory_list.clear()
        for item in self.player.inventory.items:
            self.inventory_list.addItem(f"{item.name} (Rarity: {item.rarity}, Stat Boost: {item.stat_boost})")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    player = Player("Hero", "Assassin")
    window = MainWindow(player)
    window.show()
    sys.exit(app.exec())
