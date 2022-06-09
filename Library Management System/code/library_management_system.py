from abc import ABC
from dataclasses import dataclass
import datetime
from enum import Enum

import logging
logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.DEBUG)


class BookFormat(Enum):
   HARDCOVER, PAPERBACK, AUDIO_BOOK, EBOOK, NEWSPAPER, MAGAZINE, JOURNAL = 1, 2, 3, 4, 5, 6, 7

class BookStatus(Enum):
   AVAILABLE, RESERVED, LOANED, LOST = 1, 2, 3, 4

class ReservationStatus(Enum):
   WAITING, PENDING, CANCELED, NONE = 1, 2, 3, 4

class AccountStatus(Enum):
   ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE = 1, 2, 3, 4, 5

@dataclass
class Address:
   street_address: str 
   city: str
   state: str
   zip_code: int
   country: str   

@dataclass
class Person(ABC):
   name: str 
   address: Address
   email: str
   phone: str  

@dataclass
class Constants:
   MAX_BOOKS_ISSUED_TO_A_USER: int = 5
   MAX_LENDING_DAYS: int = 10

@dataclass
class Account(ABC):
    id: str
    password: str
    person: Person
    status: AccountStatus = AccountStatus.ACTIVE   

    def reset_password(self):
        None

@dataclass
class Rack:
    number:int 
    location_identifie: str

@dataclass
class Book(ABC):
    ISBN: str 
    title: str 
    subject: str 
    publisher: str
    language: str 
    number_of_pages: int 
    authors: list[str]

@dataclass
class BookItem(Book):
    barcode: str 
    is_reference_only: bool
    borrowed: bool
    due_date: datetime.date
    price : float 
    status: BookStatus
    date_of_purchase: datetime.date
    publication_date: datetime.date
    placed_at: Rack

    def get_is_reference_only(self):
        return self.is_reference_only

    def get_is_avaialble(self):
        return self.status ==  BookStatus.AVAILABLE    

    def update_book_item_status(self, status):
        self.status = status 

    def checkout(self, member_id, due_date):
        if self.get_is_reference_only():
            logging.info("self book is Reference only and can't be issued")
            return False
        if not self.get_is_avaialble():
            logging.error("Book is already LOANED ")
            return False    
        lending =  BookLending.lend_book(self.barcode, member_id , due_date)
        self.update_book_item_status(BookStatus.LOANED)
        return lending

@dataclass
class BookReservation:
    status: BookStatus
    book_item_barcode: str 
    member_id: int 
    creation_date: datetime.date = datetime.date.today()

    @staticmethod
    def fetch_reservation_details(barcode):
        None

@dataclass
class BookLending:
    book_item_barcode: str
    member_id: int
    due_date: datetime.date 
    return_date: datetime.date = None
    creation_date: datetime.date = datetime.date.today()

    @staticmethod
    def lend_book(barcode, member_id, due_date):
        return BookLending(barcode, member_id, due_date)

    @staticmethod
    def fetch_lending_details( barcode):
        None

@dataclass
class Fine:
    book_item_barcode: str
    member_id: int
    creation_date: datetime.date = datetime.date.today()
  
    def collect_fine(self, member_id, days):
        None
       

@dataclass
class Librarian(Account):
    department= str 

    def add_book_item(self, book_item):
        None

    def block_member(self, member):
        None

    def un_block_member(self, member):
        None

@dataclass
class Member(Account):
    date_of_membership: datetime.date = datetime.date.today()
    total_books_checkedout: int = 0
  

    def get_total_books_checked_out(self):
        return self.total_books_checkedout

    def reserve_book_item(self, book_item):
        None

    def increment_total_books_checkedout(self):
        self.total_books_checkedout = self.total_books_checkedout + 1

    def decrement_total_books_checkedout(self):
        self.total_books_checkedout = self.total_books_checkedout - 1 
        

    def renew_book_item(self, book_item):
        None

    def checkout_book_item(self, book_item, due_date):
        if self.get_total_books_checked_out() >= Constants.MAX_BOOKS_ISSUED_TO_A_USER:
            logging.error("The user has already checked-out maximum number of books")
            return False
        book_reservation = BookReservation.fetch_reservation_details(
                book_item.barcode)
        if book_reservation != None and book_reservation.get_member_id() != self.get_id():
            # book item has a pending reservation from another user
            print("self book is reserved by another member")
            return False
        elif book_reservation != None:
           # book item has a pending reservation from the give member, update it
           book_reservation.update_status(ReservationStatus.COMPLETED)

        checkout_result= book_item.checkout(self.id , due_date)
        if not checkout_result :
            return False

        self.increment_total_books_checkedout()
        logging.info (f"member {self.id} loaned the book , {book_item.title}")
        return checkout_result

    def check_for_fine(self, book_item_barcode):
        book_lending = BookLending.fetch_lending_details(book_item_barcode)
        due_date = book_lending.get_due_date()
        today = datetime.date.today()
        # check if the book has been returned within the due date
        if today > due_date:
            diff = today - due_date
            diff_days = diff.days
            Fine.collect_fine(self.get_member_id(), diff_days)

    def return_book_item(self, book_item):
        #self.check_for_fine(book_item.barcode)
        book_reservation = BookReservation.fetch_reservation_details(
                book_item.barcode)
        if book_reservation != None:
            # book item has a pending reservation
            book_item.update_book_item_status(BookStatus.RESERVED)
            book_reservation.send_book_available_notification()
        book_item.update_book_item_status(BookStatus.AVAILABLE)
        self.decrement_total_books_checkedout()
        logging.info (f"member {self.id} returned the book , {book_item.title}")

    def renew_book_item(self, book_item):
        self.check_for_fine(book_item.get_barcode())
        book_reservation = BookReservation.fetch_reservation_details(
                book_item.get_barcode())
        # check if self book item has a pending reservation from another member
        if book_reservation != None and book_reservation.get_member_id() != self.get_member_id():
            print("self book is reserved by another member")
            self.decrement_total_books_checkedout()
            book_item.update_book_item_state(BookStatus.RESERVED)
            book_reservation.send_book_available_notification()
            return False
        elif book_reservation != None:
            # book item has a pending reservation from self member
            book_reservation.update_status(ReservationStatus.COMPLETED)
            BookLending.lend_book(book_item.get_bar_code(), self.get_member_id())
            book_item.update_due_date(
                    datetime.datetime.now().AddDays(Constants.MAX_LENDING_DAYS))
        return True

class Search(ABC):
  def search_by_title(self, title):
    None

  def search_by_author(self, author):
    None

  def search_by_subject(self, subject):
    None

  def search_by_pub_date(self, publish_date):
    None

@dataclass
class Catalog(Search):
    book_titles:dict
    ook_authors: dict
    book_publication_dates: dict
    book_subjects: dict

    def search_by_title(self, query):
        # return all books containing the string query in their title.
        return self.__book_titles.get(query)

    def search_by_author(self, query):
        # return all books containing the string query in their author's name.
        return self.__book_authors.get(query)




