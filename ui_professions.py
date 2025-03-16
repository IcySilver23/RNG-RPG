from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QLabel
from player import Player

class ProfessionsUI:
    def __init__(self, player):
        self.player = player
        self.professions_panel = QVBoxLayout()
        self.update_professions_panel()

    def update_professions_panel(self):
        """Update the professions panel with available professions."""
        self.professions_panel.addWidget(QLabel("Choose a Profession:"))
        for profession_name in ["Blacksmith", "Alchemist", "Enchanter"]:
            profession_button = QPushButton(profession_name, self)
            profession_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.5); color: cyan; border: 1px solid cyan;")
            profession_button.clicked.connect(lambda _, p=profession_name: self.choose_profession(p))
            self.professions_panel.addWidget(profession_button)

    def choose_profession(self, profession_name):
        """Choose a profession for the player and update the UI."""
        self.player.choose_profession(profession_name)
        self.update_professions_panel()
