## Library Management System

<img src="https://github.com/piyushmani/object-oriented-design-python/blob/a426c5935d670b7df8bb1b45a42d34474fb0abf2/Library%20Management%20System/images/library.png" width="50%" height="40%">

**Table of Contents**

- [System Requirements](https://github.com/piyushmani/object-oriented-design-python/tree/main/Library%20Management%20System#system-requirements)
- [Use case diagram](https://github.com/piyushmani/object-oriented-design-python/tree/main/Library%20Management%20System#use-case-diagram)
- [Class diagram](https://github.com/piyushmani/object-oriented-design-python/tree/main/Library%20Management%20System#class-diagram)
- [Activity diagrams](https://github.com/piyushmani/object-oriented-design-python/tree/main/Library%20Management%20System#activity-diagrams)
- [Code](https://github.com/piyushmani/object-oriented-design-python/tree/main/Library%20Management%20System#activity-diagrams)

### System Requirements

- Any library member should be able to search books by their title, author, subject category as well by the publication date.
- Any library member should be able to search books by their title, author, subject category as well by the publication date.
- Each book will have a unique identification number and other details including a rack number which will help to physically locate the book.
- There could be more than one copy of a book, and library members should be able to check-out and reserve any copy. We will call each copy of a book, a book item.
- The system should be able to retrieve information like who took a particular book or what are the books checked-out by a specific library member.
- There should be a maximum limit (5) on how many books a member can check-out.
- There should be a maximum limit (10) on how many days a member can keep a book.
- The system should be able to collect fines for books returned after the due date.
- Members should be able to reserve books that are not currently available.
- The system should be able to send notifications whenever the reserved books become available, as well as when the book is not returned within the due date.
- Each book and member card will have a unique barcode. The system will be able to read barcodes from books and members library cards.

### Use case diagram
------------
<img src="https://github.com/piyushmani/object-oriented-design-python/blob/f7e3d15691bad10da22988c750d75347172cd4e3/Library%20Management%20System/images/Uml_Diagram%20(3).svg" width="40%" height="20%">


### Class diagram
------------

<img src="https://github.com/piyushmani/object-oriented-design-python/blob/97c102a4bc2aa0c31c1ebfa002ed49eb42f140a3/Library%20Management%20System/images/class_diagram.svg" width="60%" height="20%">

### Activity diagrams
------------

####  Book checkout 
```mermaid
%%{init: { "theme": "forest","flowchart": {"nodeSpacing":10, "rankSpacing":20,"curve": "basic","useMaxWidth":true}} }%%
flowchart TD
    A[Start] --> B
    B(Member scan their library card) --> C
    C(Scan barcode of book) --> D
    D{{Checks if book can be issued or not ??}}
    E{{ Checks numner of book  issued  to the member}}
    F{{Checks if book has been reserved by any other member ??}}
    G[Create book checkout transaction]
    H[Update Book status to Loaned]
    I[Increment book issued to the member]
    J[Mark reservation completed that member has made against this book]
    K[Show success message]
    D -->|No| Y 
    D -->|Yes| E
    E -->|max quato Excedded|Y 
    E -->|else| F
    F -->|Yes | Y 
    F -->|No| G -->H -->I -->J -->K-->Z
    Y[Show error message]
    Z[End]
    Y -->Z 
```
#### Return a book
```mermaid
%%{init: { "theme": "forest","flowchart": {"nodeSpacing":10, "rankSpacing":20,"curve": "basic","useMaxWidth":true}} }%%
flowchart TD
    A[Start] --> B
    B(Member scan barcode of the book) --> C
    C(System fetches book`s details ) --> D
    D{{System checks if book is being returned within the due date ??}}
    E(Calculate fine)
    F(Create transaction for the fine collection)
    G(Collect fine)
    H{{ System decrements the number of book issued to the member}}
    I{{System checks if book is reserved by any member ??}}
    J(System update the status of the book to reserved)
    K(System update the status of the book to available)
    L(system sends notification to the member who has reserved the book about the availibilty of the book)
    Z(End)
    D -->|No| E
    D --> |Yes| H
    E -->F-->G-->H
    H -->I
    I -->|No| K -->Z
    I -->|Yes|J
    J  -->L -->Z
```
#### Renew a book
```mermaid
%%{init: { "theme": "forest","flowchart": {"nodeSpacing":10, "rankSpacing":20,"curve": "basic","useMaxWidth":true}} }%%
flowchart TD
    A[Start] 
    B(Member scans their library card through barcode reade) 
    C(Member scans barcode of the book and selects to renew the book)
    D(System fetches book`s details ) 
    E{{Check if the book has been returned within due date ??}}
    F[Calculate fine]
    G[Create transactionyes for fine collection]
    H[Collect fine]
    I[ Check if the book has been reserved by any other member ??]
    J[Show error message that the book can't be issued]
    K[Update the status of the book to 'Reserved']
    L[Create book checkout transaction with new due date]
    M[Send notification to thee member who has reserved the book that the book has become available]
    Z(End)

    A-->B-->C-->D-->E
    E --> |No| F -->G-->H-->I
    E --> |Yes| I
    I -->|yes| J-->K-->M-->Z
    I-->|No|L-->Z
```

### Code

------------



 Below is the code for book checkout, book return and book renew.
 
 > ***Note => In below code the database implementation and payment implementation are skiped.***
 
 ###### Enums and Constants
 
 
 ```python
from abc import ABC
from enum import Enum
from dataclasses import dataclass

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
    
```
###### Rack, Book and BookItem

```python
from abc import ABC
from dataclasses import dataclass
import datetime

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
    is_reference_only: str
    borrowed: bool
    due_date: datetime.date
    price : float 
    status: BookStatus
    date_of_purchase: datetime.date
    publication_date: datetime.date
    placed_at: Rack
```

###### Account, Member, and Librarian

```python
from abc import ABC
from dataclasses import dataclass
import datetime

@dataclass
class Librarian(Account):
    department= str 

    def add_book_item(self, book_item):
        None

    def block_member(self, member):
        None

    def un_block_member(self, member):
        None

class Member(Account):
    date_of_membership: datetime.date = datetime.date.today()
    total_books_checkedout: int = 0
  

    def get_total_books_checked_out(self):
        return self.total_books_checkedout

    def reserve_book_item(self, book_item):
        None

    def increment_total_books_checkedout(self):
        None

    def renew_book_item(self, book_item):
        None

    def checkout_book_item(self, book_item):
        if self.get_total_books_checked_out() >= Constants.MAX_BOOKS_ISSUED_TO_A_USER:
            print("The user has already checked-out maximum number of books")
            return False
        book_reservation = BookReservation.fetch_reservation_details(
                book_item.get_barcode())
        if book_reservation != None and book_reservation.get_member_id() != self.get_id():
            # book item has a pending reservation from another user
            print("self book is reserved by another member")
            return False
        elif book_reservation != None:
           # book item has a pending reservation from the give member, update it
           book_reservation.update_status(ReservationStatus.COMPLETED)

        if not book_item.checkout(self.get_id()):
            return False

        self.increment_total_books_checkedout()
        return True

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
        self.check_for_fine(book_item.get_barcode())
        book_reservation = BookReservation.fetch_reservation_details(
                book_item.get_barcode())
        if book_reservation != None:
            # book item has a pending reservation
            book_item.update_book_item_status(BookStatus.RESERVED)
            book_reservation.send_book_available_notification()
        book_item.update_book_item_status(BookStatus.AVAILABLE)

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
```
###### BookReservation, BookLending, and Fine

```python
from abc import ABC
from dataclasses import dataclass
import datetime

@dataclass
class BookReservation:
    status: BookStatus
    book_item_barcode: str 
    member_id: int 
    creation_date: datetime.date = datetime.date.today()
    
    def fetch_reservation_details(self, barcode):
        None

@dataclass
class BookLending:
    book_item_barcode: str
    member_id: int
    due_date: datetime.date 
    return_date: datetime.date = None
    creation_date: datetime.date = datetime.date.today()

    def lend_book(self, barcode, member_id):
        None

    def fetch_lending_details(self, barcode):
        None

@dataclass
class Fine:
    book_item_barcode: str
    member_id: int
    creation_date: datetime.date = datetime.date.today()
  
    def collect_fine(self, member_id, days):
        None
```

###### Search and Catalog

```python
from abc import ABC
from dataclasses import dataclass

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
    book_authors: dict
    book_publication_dates: dict
    book_subjects: dict

    def search_by_title(self, query):
        # return all books containing the string query in their title.
        return self.__book_titles.get(query)

    def search_by_author(self, query):
        # return all books containing the string query in their author's name.
        return self.__book_authors.get(query)
```






