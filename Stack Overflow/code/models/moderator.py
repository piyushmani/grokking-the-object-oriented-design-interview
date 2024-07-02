# models/moderator.py
from models.member import Member
from models.question import Question
from enums.question_status import QuestionStatus

class Moderator(Member):
    def close_question(self, question: Question, remark):
        if question.status != QuestionStatus.CLOSED:
            question.status = QuestionStatus.CLOSED
            question.closing_remark = remark
            print(f"Question '{question.title}' closed by {self.account.name}.")
        else:
            print(f"Question '{question.title}' is already closed.")

    def undelete_question(self, question: Question):
        if question.status == QuestionStatus.DELETED:
            question.status = QuestionStatus.OPEN
            print(f"Question '{question.title}' undeleted by {self.account.name}.")
        else:
            print(f"Question '{question.title}' is not deleted.")
