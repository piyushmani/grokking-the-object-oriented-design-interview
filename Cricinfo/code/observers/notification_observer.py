from ..models.notification import Notification

class NotificationObserver:
    def notify(self, notification: Notification):
        notification.send()
