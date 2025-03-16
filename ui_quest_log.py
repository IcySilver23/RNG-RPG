from PyQt6.QtWidgets import QVBoxLayout, QLabel, QProgressBar
from quest import QuestSystem

class QuestLogUI:
    def __init__(self, player):
        self.player = player
        self.quest_log = QVBoxLayout()
        self.update_quest_log()

    def update_quest_log(self):
        """Update the quest log with active and completed quests."""
        self.quest_log.addWidget(QLabel("Quest Log:"))
        for quest in self.player.active_quests:
            quest_label = QLabel(f"{quest.name} - {quest.objective}")
            quest_label.setStyleSheet("color: cyan;")
            self.quest_log.addWidget(quest_label)
            progress_bar = QProgressBar(self)
            progress_bar.setMaximum(100)
            progress_bar.setValue(quest.progress)
            progress_bar.setFormat(f"{quest.progress}%")
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
            self.quest_log.addWidget(progress_bar)
            reward_label = QLabel(f"Reward: {quest.reward['gold']} gold, {quest.reward['exp']} XP")
            reward_label.setStyleSheet("color: cyan;")
            self.quest_log.addWidget(reward_label)
