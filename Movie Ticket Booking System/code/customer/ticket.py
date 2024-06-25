from dataclasses import dataclass
from .booking import Booking
from cinema.seat import Seat

@dataclass
class MovieTicket:
    booking: Booking
    seat: Seat

    def __str__(self):
        return f"Ticket for {self.booking.show_time.start_time} at Seat {self.seat.number}"
