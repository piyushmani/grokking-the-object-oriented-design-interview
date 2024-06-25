from cinema.city import City
from cinema.cinema import Cinema
from cinema.hall import Hall
from cinema.seat import Seat
from cinema.movie import Movie
from cinema.showtime import ShowTime
from customer.customer import Customer
from customer.ticket import MovieTicket
from payment.payment import Payment
from payment.credit_card_payment import CreditCardPayment
from payment.cash_payment import CashPayment
from catalog.catalog import Catalog
from search.search import Search
from notification.notification import Notification

def main():
    # Setup Catalog
    catalog = Catalog()

    # Setup Cities and Cinemas
    hall_1 = Hall(number=1, seats=[Seat(number=i) for i in range(1, 101)])
    hall_2 = Hall(number=2, seats=[Seat(number=i) for i in range(1, 151)])

    cinema_1 = Cinema(name="Cinema One", city="New York", halls=[hall_1, hall_2], movies=[])
    cinema_2 = Cinema(name="Cinema Two", city="New York", halls=[hall_1], movies=[])

    catalog.add_cinema(cinema_1)
    catalog.add_cinema(cinema_2)

    # Setup Movies
    movie_1 = Movie(title="The Avengers", language="English", genre="Action", release_date="2021-04-25", shows=[
        ShowTime(start_time="10:00 AM", end_time="12:30 PM"),
        ShowTime(start_time="01:00 PM", end_time="03:30 PM")
    ])
    movie_2 = Movie(title="Inception", language="English", genre="Sci-Fi", release_date="2010-07-16", shows=[
        ShowTime(start_time="04:00 PM", end_time="06:30 PM"),
        ShowTime(start_time="07:00 PM", end_time="09:30 PM")
    ])

    # Adding movies to cinemas
    cinema_1.movies.append(movie_1)
    cinema_2.movies.append(movie_2)

    # Adding movies to the catalog
    catalog.add_movie(movie_1)
    catalog.add_movie(movie_2)

    # Setup Customer
    customer = Customer(name="John Doe", email="john@example.com", phone="1234567890")

    # Search Movies
    search_results = Search.search_movies(catalog.movies, title="Inception", city_name="New York", cinemas=catalog.cinemas)
    print(f"Search results: {[movie.title for movie in search_results]}")

    # Book a Ticket
    cinema = catalog.get_cinemas_in_city("New York")[1]  # Ensure selecting the correct cinema
    show_time = cinema.get_showtimes("Inception")[0]  # Check if showtimes are available for "Inception"

    seat = cinema.halls[0].seats[0]  # Just as an example
    payment_method = CreditCardPayment()

    payment = Payment(amount=12.50, method=payment_method)
    booking = customer.book_tickets(cinema, show_time, [seat], payment)
    ticket = MovieTicket(booking=booking, seat=seat)
    print(f"Booked Ticket: {ticket}")

    # Send Notification
    notification = Notification(message="Your booking is confirmed!")
    notification.send(recipient=customer.email)

if __name__ == "__main__":
    main()
