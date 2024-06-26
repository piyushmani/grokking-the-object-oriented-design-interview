from dataclasses import dataclass
import datetime

@dataclass
class Notification:
    notification_id: int
    content: str
    created_on: datetime.date = datetime.date.today()

    def send_notification(self, account):
        pass
