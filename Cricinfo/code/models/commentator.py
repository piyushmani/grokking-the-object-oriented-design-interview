from dataclasses import dataclass, field
from typing import List, Optional
from .match import Match

@dataclass
class Commentator:
    commentator_id: int
    name: str
    specialization: str
    matches_commented: int

    def increment_matches_commented(self):
        self.matches_commented += 1

@dataclass
class Commentary:
    commentary_id: int
    match: Match
    comments: List[str] = field(default_factory=list)

    def add_comment(self, comment: str):
        self.comments.append(comment)

class CommentaryService:
    def add_commentary(self, commentary: Commentary, commentator: Commentator, comment: str):
        full_comment = f"{commentator.name}: {comment}"
        commentary.add_comment(full_comment)
        commentator.increment_matches_commented()

    def get_latest_commentary(self, commentary: Commentary) -> Optional[str]:
        return commentary.comments[-1] if commentary.comments else None