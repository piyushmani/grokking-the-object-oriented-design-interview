from dataclasses import dataclass, field
from typing import List
from .booking import Booking

@dataclass
class Customer:
    name: str
    email: str
    phone: str
    bookings: List[Booking] = field(default_factory=list)

    def make_payment(self, amount: float, payment_method: "PaymentMethod") -> bool:
        return payment_method.process_payment(amount)

    def book_tickets(self, cinema: "Cinema", show_time: "ShowTime", seats: List["Seat"], payment: "Payment") -> "Booking":
        if not all(seat.is_booked == False for seat in seats):
            raise ValueError("Some seats are already booked")
        for seat in seats:
            seat.is_booked = True

        booking = Booking(customer=self, show_time=show_time, seats=seats)
        self.bookings.append(booking)
        if payment.process():
            return booking
        else:
            for seat in seats:
                seat.is_booked = False
            raise ValueError("Payment failed")
