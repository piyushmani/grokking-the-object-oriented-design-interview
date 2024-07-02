# models/question.py
from dataclasses import dataclass, field
import datetime
from models.member import Member
from models.bounty import Bounty
from enums.question_status import QuestionStatus
from enums.question_closing_remark import QuestionClosingRemark

@dataclass
class Question:
    title: str
    description: str
    bounty: Bounty
    asking_member: Member
    view_count: int = 0
    vote_count: int = 0
    creation_time: datetime.datetime = field(default_factory=datetime.datetime.now)
    update_time: datetime.datetime = field(default_factory=datetime.datetime.now)
    status: QuestionStatus = QuestionStatus.OPEN
    closing_remark: QuestionClosingRemark = QuestionClosingRemark.DUPLICATE
    photos: list = field(default_factory=list)
    comments: list = field(default_factory=list)
    answers: list = field(default_factory=list)

    def close(self):
        if self.status != QuestionStatus.CLOSED:
            self.status = QuestionStatus.CLOSED
            print(f"Question '{self.title}' closed.")
        else:
            print(f"Question '{self.title}' is already closed.")

    def undelete(self):
        if self.status == QuestionStatus.DELETED:
            self.status = QuestionStatus.OPEN
            print(f"Question '{self.title}' undeleted.")
        else:
            print(f"Question '{self.title}' is not deleted.")

    def add_comment(self, comment):
        self.comments.append(comment)
        print(f"Comment added to question '{self.title}'.")

    def add_bounty(self, bounty: Bounty):
        self.bounty = bounty
        print(f"Bounty added to question '{self.title}'.")

    def search(self, query: str):
        if query in self.title or query in self.description:
            return self
        return None
