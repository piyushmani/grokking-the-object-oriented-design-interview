# models/notification.py
from dataclasses import dataclass, field
import datetime

@dataclass
class Notification:
    notification_id: int
    content: str
    created_on: datetime.datetime = field(default_factory=datetime.datetime.now)

    def send_notification(self):
        print(f"Sending notification: {self.content}")
