from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QProgressBar, QInputDialog, QTextEdit
from PyQt6.QtGui import QFont, QColor, QPalette, QGraphicsDropShadowEffect
from PyQt6.QtCore import Qt, QTimer
from player import Player
from dungeon import dungeons

class MainWindow(QMainWindow):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.setWindowTitle("Solo Leveling RPG")
        self.setGeometry(100, 100, 800, 600)
        self.set_dark_theme()

        # Title Label
        self.title_label = QLabel("Solo Leveling RPG", self)
        self.title_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        self.title_label.setStyleSheet("color: cyan;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.apply_shadow_effect(self.title_label)

        # Player Stats Panel
        self.stats_panel = QLabel(self)
        self.update_stats_panel()

        # Experience Bar
        self.exp_bar = QProgressBar(self)
        self.exp_bar.setMaximum(100)
        self.exp_bar.setValue(self.player.exp)
        self.exp_bar.setFormat("EXP: %v/%m")
        self.exp_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid purple;
                border-radius: 5px;
                text-align: center;
                background-color: rgba(51, 51, 51, 0.8);
                color: white;
            }
            QProgressBar::chunk {
                background-color: purple;
            }
        """)

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
                background-color: rgba(51, 51, 51, 0.8);
                color: white;
            }
            QProgressBar::chunk {
                background-color: cyan;
            }
        """)

        # Allocate Stat Points Button
        self.allocate_button = QPushButton("Allocate Stat Points", self)
        self.allocate_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.5); color: cyan; border: 1px solid cyan;")
        self.allocate_button.clicked.connect(self.allocate_stat_points)

        # Roll for Loot Button
        self.roll_button = QPushButton("Roll for Loot", self)
        self.roll_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.5); color: cyan; border: 1px solid cyan;")
        self.roll_button.clicked.connect(self.roll_for_loot)

        # Combat Log Panel
        self.combat_log = QTextEdit(self)
        self.combat_log.setReadOnly(True)
        self.combat_log.setStyleSheet("""
            QTextEdit {
                border: 2px solid cyan;
                border-radius: 5px;
                padding: 5px;
                background-color: rgba(51, 51, 51, 0.8);
                color: white;
            }
        """)

        # Sidebar with buttons for different game sections
        self.sidebar = QVBoxLayout()
        self.sidebar.setSpacing(10)
        self.sidebar.setContentsMargins(10, 10, 10, 10)
        self.sidebar.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.inventory_button = QPushButton("Inventory", self)
        self.inventory_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.5); color: cyan; border: 1px solid cyan;")
        self.sidebar.addWidget(self.inventory_button)

        self.stats_button = QPushButton("Stats", self)
        self.stats_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.5); color: cyan; border: 1px solid cyan;")
        self.sidebar.addWidget(self.stats_button)

        self.dungeon_button = QPushButton("Dungeons", self)
        self.dungeon_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.5); color: cyan; border: 1px solid cyan;")
        self.sidebar.addWidget(self.dungeon_button)

        self.log_button = QPushButton("Combat Log", self)
        self.log_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.5); color: cyan; border: 1px solid cyan;")
        self.sidebar.addWidget(self.log_button)

        self.skill_tree_button = QPushButton("Skill Tree", self)
        self.skill_tree_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.5); color: cyan; border: 1px solid cyan;")
        self.sidebar.addWidget(self.skill_tree_button)

        self.professions_button = QPushButton("Professions", self)
        self.professions_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.5); color: cyan; border: 1px solid cyan;")
        self.sidebar.addWidget(self.professions_button)

        self.enhancement_button = QPushButton("Enhancement", self)
        self.enhancement_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.5); color: cyan; border: 1px solid cyan;")
        self.sidebar.addWidget(self.enhancement_button)

        # Main layout
        main_layout = QHBoxLayout()
        main_layout.addLayout(self.sidebar)

        content_layout = QVBoxLayout()
        content_layout.addWidget(self.title_label)
        content_layout.addWidget(self.stats_panel)
        content_layout.addWidget(self.exp_bar)
        content_layout.addWidget(self.mana_bar)
        content_layout.addWidget(self.allocate_button)
        content_layout.addWidget(self.roll_button)
        content_layout.addWidget(self.combat_log)

        main_layout.addLayout(content_layout)

        container = QWidget()
        container.setLayout(main_layout)
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
        self.update_stats_panel()
        self.update_inventory_grid()
        self.update_combat_log(f"You received: {item.name} (Rarity: {item.rarity}, Stat Boost: {item.stat_boost})")
        print(f"You received: {item}")

    def update_stats_panel(self):
        """Update the player stats panel with the current stats."""
        stats_text = (
            f"Name: {self.player.name}\n"
            f"Level: {self.player.level}\n"
            f"HP: {self.player.hp}\n"
            f"Mana: {self.player.mana}\n"
            f"STR: {self.player.stats['STR']}\n"
            f"AGI: {self.player.stats['AGI']}\n"
            f"INT: {self.player.stats['INT']}\n"
            f"DEF: {self.player.stats['DEF']}\n"
            f"Gold: {self.player.currency}\n"
            f"Stat Points: {self.player.stat_points}"
        )
        self.stats_panel.setText(stats_text)

    def update_combat_log(self, message):
        """Update the combat log with a new message."""
        self.combat_log.append(message)

    def regenerate_mana(self):
        """Regenerate mana over time."""
        if self.player.mana < self.player.stats['INT'] * 10:
            self.player.mana += 1
            self.mana_bar.setValue(self.player.mana)
            self.update_stats_panel()

    def allocate_stat_points(self):
        """Allocate stat points to a specific stat."""
        stat, ok = QInputDialog.getText(self, "Allocate Stat Points", "Enter the stat to allocate points to (STR, AGI, INT, DEF):")
        if ok and stat in self.player.stats:
            points, ok = QInputDialog.getInt(self, "Allocate Stat Points", f"Enter the number of points to allocate to {stat}:")
            if ok:
                self.player.allocate_stat_points(stat, points)
                self.update_stats_panel()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    player = Player("Hero", "Assassin")
    window = MainWindow(player)
    window.show()
    sys.exit(app.exec())

