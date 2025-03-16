from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QLabel, QProgressBar
from battle_pass import BattlePass, battle_pass_rewards

class BattlePassUI:
    def __init__(self, player):
        self.player = player
        self.battle_pass = BattlePass(season=1, levels=20, rewards=battle_pass_rewards)
        self.battle_pass_panel = QVBoxLayout()
        self.update_battle_pass_panel()

    def update_battle_pass_panel(self):
        """Update the Battle Pass panel with progress and rewards."""
        self.battle_pass_panel.addWidget(QLabel(f"Battle Pass Season {self.battle_pass.season}"))
        progress_bar = QProgressBar(self)
        progress_bar.setMaximum(self.battle_pass.levels)
        progress_bar.setValue(self.battle_pass.current_level)
        progress_bar.setFormat(f"Level {self.battle_pass.current_level}/{self.battle_pass.levels}")
        progress_bar.setStyleSheet("""
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
        self.battle_pass_panel.addWidget(progress_bar)

        for level in range(1, self.battle_pass.levels + 1):
            reward = self.battle_pass.rewards.get(level, "No reward")
            reward_label = QLabel(f"Level {level}: {reward}")
            reward_label.setStyleSheet("color: cyan;")
            self.battle_pass_panel.addWidget(reward_label)

        gain_level_button = QPushButton("Gain Battle Pass Level", self)
        gain_level_button.setStyleSheet("background-color: rgba(0, 0, 0, 0.5); color: cyan; border: 1px solid cyan;")
        gain_level_button.clicked.connect(self.gain_battle_pass_level)
        self.battle_pass_panel.addWidget(gain_level_button)

    def gain_battle_pass_level(self):
        """Gain a level in the Battle Pass and update the UI."""
        self.battle_pass.gain_level(self.player)
        self.update_battle_pass_panel()
