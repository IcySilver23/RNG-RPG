from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QListWidget, QListWidgetItem, QComboBox, QTextEdit, QProgressBar
from PyQt6.QtGui import QFont, QColor, QPalette, QGraphicsDropShadowEffect
from PyQt6.QtCore import Qt, QTimer
from items import roll_for_loot
from player import Player
from dungeon import dungeons

class MainWindow(QMainWindow):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.setWindowTitle("Solo Leveling RNG")
        self.setGeometry(100, 100, 600, 600)
        self.set_dark_theme()

        # Title Label
        self.title_label = QLabel("Solo Leveling RNG", self)
        self.title_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        self.title_label.setStyleSheet("color: cyan;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.apply_shadow_effect(self.title_label)

        # Player Stats Label
        self.stats_label = QLabel(self)
        self.update_stats_label()

        # Mana Bar
        self.mana_bar = QProgressBar(self)
        self.mana_bar.setMaximum(self.player.stats['INT'] * 10)
        self.mana_bar.setValue(self.player.mana)
        self.mana_bar.setFormat("Mana: %v/%m")
        self.mana_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid cyan;
                border-radius: 5px;
                text-align: center;
                background-color: #333;
                color: white;
            }
            QProgressBar::chunk {
                background-color: cyan;
            }
        """)

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

        # Dungeon Selection ComboBox
        self.dungeon_combo = QComboBox(self)
        self.dungeon_combo.addItems([f"{dungeon.name} ({dungeon.difficulty})" for dungeon in dungeons])
        self.dungeon_combo.currentIndexChanged.connect(self.select_dungeon)

        # Combat Log Panel
        self.combat_log = QTextEdit(self)
        self.combat_log.setReadOnly(True)
        self.combat_log.setStyleSheet("""
            QTextEdit {
                border: 2px solid cyan;
                border-radius: 5px;
                padding: 5px;
                background-color: #333;
                color: white;
            }
        """)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.stats_label)
        layout.addWidget(self.mana_bar)
        layout.addWidget(self.roll_button)
        layout.addWidget(self.inventory_list)
        layout.addWidget(self.dungeon_combo)
        layout.addWidget(self.combat_log)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.selected_dungeon = dungeons[0]

        # Mana Regeneration Timer
        self.mana_regen_timer = QTimer(self)
        self.mana_regen_timer.timeout.connect(self.regenerate_mana)
        self.mana_regen_timer.start(1000)  # Regenerate mana every second

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

    def apply_shadow_effect(self, widget):
        """Apply a shadow effect to a widget."""
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setColor(QColor("cyan"))
        shadow.setOffset(0, 0)
        widget.setGraphicsEffect(shadow)

    def roll_for_loot(self):
        """Roll for loot and update the player's inventory and stats."""
        item = roll_for_loot(self.selected_dungeon.difficulty)
        self.player.add_to_inventory(item)
        self.update_stats_label()
        self.update_inventory_list()
        self.update_combat_log(f"You received: {item.name} (Rarity: {item.rarity}, Stat Boost: {item.stat_boost})")
        print(f"You received: {item}")

    def update_stats_label(self):
        """Update the player stats label with the current stats."""
        stats_text = f"Name: {self.player.name}\nLevel: {self.player.level}\nHP: {self.player.hp}\nMana: {self.player.mana}\nGold: {self.player.currency}"
        self.stats_label.setText(stats_text)

    def update_inventory_list(self):
        """Update the inventory list with the current items."""
        self.inventory_list.clear()
        rarity_colors = {
            "Common": "white",
            "Rare": "blue",
            "Epic": "purple",
            "Legendary": "gold"
        }
        for item in self.player.inventory.items:
            list_item = QListWidgetItem(f"{item.name} (Rarity: {item.rarity}, Stat Boost: {item.stat_boost})")
            list_item.setForeground(QColor(rarity_colors.get(item.rarity, "white")))
            self.inventory_list.addItem(list_item)

    def select_dungeon(self, index):
        """Select a dungeon based on the combo box index."""
        self.selected_dungeon = dungeons[index]
        self.update_combat_log(f"Selected dungeon: {self.selected_dungeon.name} ({self.selected_dungeon.difficulty})")
        print(f"Selected dungeon: {self.selected_dungeon.name} ({self.selected_dungeon.difficulty})")

    def update_combat_log(self, message):
        """Update the combat log with a new message."""
        self.combat_log.append(message)

    def regenerate_mana(self):
        """Regenerate mana over time."""
        if self.player.mana < self.player.stats['INT'] * 10:
            self.player.mana += 1
            self.mana_bar.setValue(self.player.mana)
            self.update_stats_label()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    player = Player("Hero", "Assassin")
    window = MainWindow(player)
    window.show()
    sys.exit(app.exec())
