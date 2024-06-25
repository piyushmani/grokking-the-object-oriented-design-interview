from dataclasses import dataclass
from typing import List
from cinema.seat import Seat
from cinema.showtime import ShowTime

@dataclass
class Booking:
    customer: "Customer"
    show_time: ShowTime
    seats: List[Seat]
