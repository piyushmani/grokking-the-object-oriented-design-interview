# enums/question_status.py
from enum import Enum

class QuestionStatus(Enum):
    OPEN = 1
    CLOSED = 2
    ON_HOLD = 3
    DELETED = 4
