from dataclasses import dataclass

@dataclass
class Notification:
    message: str

    def send(self, recipient: str):
        print(f"Sending notification to {recipient}: {self.message}")
