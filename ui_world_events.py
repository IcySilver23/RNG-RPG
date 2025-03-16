from PyQt6.QtWidgets import QVBoxLayout, QLabel
from events import WorldEvent

class WorldEventsUI:
    def __init__(self):
        self.world_events_panel = QVBoxLayout()
        self.update_world_events_panel()

    def update_world_events_panel(self):
        """Update the world events panel with active global events."""
        self.world_events_panel.addWidget(QLabel("Active World Events:"))
        for event in WorldEvent.active_events:
            event_label = QLabel(f"{event.event_type}: {event.description}")
            event_label.setStyleSheet("color: cyan;")
            self.world_events_panel.addWidget(event_label)
