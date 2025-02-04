from dataclasses import dataclass
from typing import Optional

@dataclass
class Run:
    runs: int
    extras: int = 0
    extra_type: Optional[str] = None  # e.g., wide, no-ball, leg-bye, etc.
