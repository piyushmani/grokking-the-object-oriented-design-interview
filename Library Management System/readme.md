## Library Management System

<img src="https://github.com/piyushmani/object-oriented-design-python/blob/a426c5935d670b7df8bb1b45a42d34474fb0abf2/Library%20Management%20System/images/library.png" width="50%" height="40%">

**Table of Contents**

- [System Requirements](https://github.com/hillaryfraley/jobbriefings#purpose)
- [Use case diagram](https://github.com/hillaryfraley/jobbriefings#scope)
- [Class diagram](https://github.com/hillaryfraley/jobbriefings#work-practice)
- [Activity diagrams](https://github.com/hillaryfraley/jobbriefings#daily-briefing)
- [Code](https://github.com/hillaryfraley/jobbriefings#daily-briefing)

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




