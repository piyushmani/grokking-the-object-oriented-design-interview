# models/comment.py
from dataclasses import dataclass, field
import datetime
from models.member import Member

@dataclass
class Comment:
    text: str
    member: Member
    flag_count: int = 0
    vote_count: int = 0
    creation_time: datetime.datetime = field(default_factory=datetime.datetime.now)

    def increment_vote_count(self):
        self.vote_count += 1
        print(f"Vote count for comment '{self.text}' incremented to {self.vote_count}.")
