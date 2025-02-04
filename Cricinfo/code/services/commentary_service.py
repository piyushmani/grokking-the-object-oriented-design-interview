from typing import Optional
from models.commentator import Commentator, Commentary

class CommentaryService:
    def add_commentary(self, commentary: Commentary, commentator: Commentator, comment: str):
        full_comment = f"{commentator.name}: {comment}"
        commentary.add_comment(full_comment)
        commentator.increment_matches_commented()

    def get_latest_commentary(self, commentary: Commentary) -> Optional[str]:
        return commentary.comments[-1] if commentary.comments else None