from dataclasses import dataclass

@dataclass
class Seat:
    number: int
    is_booked: bool = False
