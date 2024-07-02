# models/photo.py
from dataclasses import dataclass, field
import datetime
from models.member import Member

@dataclass
class Photo:
    photo_id: int
    photo_path: str
    creating_member: Member
    created_on: datetime.datetime = field(default_factory=datetime.datetime.now)

    def delete(self):
        print(f"Photo {self.photo_id} deleted.")
