# models/answer.py
from dataclasses import dataclass, field
import datetime
from models.member import Member

@dataclass
class Answer:
    answer_text: str
    member: Member
    accepted: bool = False
    vote_count: int = 0
    flag_count: int = 0
    creation_time: datetime.datetime = field(default_factory=datetime.datetime.now)
    photos: list = field(default_factory=list)

    def increment_vote_count(self):
        self.vote_count += 1
        print(f"Vote count for answer '{self.answer_text}' incremented to {self.vote_count}.")
