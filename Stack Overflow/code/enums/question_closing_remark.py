# enums/question_closing_remark.py
from enum import Enum

class QuestionClosingRemark(Enum):
    DUPLICATE = 1
    OFF_TOPIC = 2
    TOO_BROAD = 3
    NOT_CONSTRUCTIVE = 4
    NOT_A_REAL_QUESTION = 5
    PRIMARILY_OPINION_BASED = 6
