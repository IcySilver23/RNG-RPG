from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QLabel
from player import Player
from dungeon import dungeons

class DungeonSelectionUI:
    def __init__(self, player):
        self.player = player
        self.dungeon_selection_panel = QVBoxLayout()
        self.update_dungeon_selection_panel()

    def update_dungeon_selection_panel(self):
        """Update the dungeon selection panel with available dungeons."""
        self.dungeon_selection_panel.addWidget(QLabel("Select a Dungeon:"))
        for dungeon in dungeons:
            dungeon_button = QPushButton(f"{dungeon.name} (Difficulty: {dungeon.difficulty})", self)
            dungeon_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.5); color: cyan; border: 1px solid cyan;")
            dungeon_button.clicked.connect(lambda _, d=dungeon: self.select_dungeon(d))
            self.dungeon_selection_panel.addWidget(dungeon_button)

        self.enter_dungeon_button = QPushButton("Enter Dungeon", self)
        self.enter_dungeon_button.setStyleSheet("""
            background-color: rgba(0, 0, 0, 0.5);
            color: cyan;
            border: 1px solid cyan;
            font-weight: bold;
            text-shadow: 0 0 10px cyan;
        """)
        self.enter_dungeon_button.clicked.connect(self.enter_dungeon)
        self.dungeon_selection_panel.addWidget(self.enter_dungeon_button)

    def select_dungeon(self, dungeon):
        """Select a dungeon and update the selected dungeon."""
        self.selected_dungeon = dungeon
        self.update_combat_log(f"Selected dungeon: {self.selected_dungeon.name} (Difficulty: {self.selected_dungeon.difficulty})")
        print(f"Selected dungeon: {self.selected_dungeon.name} (Difficulty: {self.selected_dungeon.difficulty})")

    def enter_dungeon(self):
        """Enter the selected dungeon."""
        if self.selected_dungeon:
            self.selected_dungeon.enter(self.player)
            self.update_combat_log(f"Entered dungeon: {self.selected_dungeon.name}")
            print(f"Entered dungeon: {self.selected_dungeon.name}")

    def update_combat_log(self, message):
        """Update the combat log with a new message."""
        self.combat_log.append(message)
