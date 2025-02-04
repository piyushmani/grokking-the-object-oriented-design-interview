from abc import ABC, abstractmethod
from typing import List

# Observer Pattern
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class EmailNotification(Observer):
    def __init__(self, email: str):
        self.email = email

    def update(self, message: str):
        print(f"Sending email to {self.email}: {message}")

class PushNotification(Observer):
    def __init__(self, phone: str):
        self.phone = phone

    def update(self, message: str):
        print(f"Sending push notification to {self.phone}: {message}")

class NotificationService:
    def __init__(self):
        self._observers: List[Observer] = []

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)