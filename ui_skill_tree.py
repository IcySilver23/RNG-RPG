from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem
from player import Player

class SkillTreeUI:
    def __init__(self, player):
        self.player = player
        self.skill_tree = QTreeWidget()
        self.skill_tree.setHeaderLabels(["Skill", "Description", "Cooldown"])
        self.update_skill_tree()

    def update_skill_tree(self):
        """Update the skill tree with the player's skills."""
        self.skill_tree.clear()
        for skill in self.player.skills:
            skill_item = QTreeWidgetItem([skill.name, skill.description, f"{skill.cooldown} sec"])
            self.skill_tree.addTopLevelItem(skill_item)
