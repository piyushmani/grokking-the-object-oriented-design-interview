
**Table of Contents**

- [System Requirements](#system-requirements)
- [Class diagram](#class-diagram)
- [Activity diagrams](#activity-diagrams)
- [Code](#code)

### System Requirements
- The parking lot should have multiple floors where customers can park their cars.
- The parking lot should have multiple entry and exit points.
- Customers can collect a parking ticket from the entry points and can pay the parking fee at the exit points on their way out.
- Customers can pay the tickets at the automated exit panel or to the parking attendant.
- Customers can pay via both cash and credit cards.
- Customers should also be able to pay the parking fee at the customer’s info portal on each floor. If the customer has paid at the info portal, they don’t have to pay at the exit.
-The system should not allow more vehicles than the maximum capacity of the parking lot. If the parking is full, the system should be able to show a message at the entrance panel and on the parking display board on the ground floor.
- Each parking floor will have many parking spots. The system should support multiple types of parking spots such as Compact, Large, Handicapped, Motorcycle, etc.
- The Parking lot should have some parking spots specified for electric cars. These spots should have an electric panel through which customers can pay and charge their vehicles.
- The system should support parking for different types of vehicles like car, truck, van, motorcycle, etc.
- Each parking floor should have a display board showing any free parking spot for each spot type.
- The system should support a per-hour parking fee model. For example, customers have to pay $4 for the first hour, $3.5 for the second and third hours, and $2.5 for all the remaining hours.

### Class diagram
------------

```mermaid
%%{init: { "theme": "neutral"} }%%
classDiagram
    direction LR
    class ParkingLot{
      id: string
      address: Location
      addParkingFloor()
      addEnterancePanel()
      getNewParkingTicket()
      isFull() 
    }
    class ParkingFloor{
      name: string
      updateDisplayBoard()
      addParkingSiot()
      assignVehicleToSlot()
      freeSlot()
    }
    class ParkingDisplayBoard{
      id: string
      handicappedFreeSpot()
      compactFreeSpot()
      largeFreeSpot()
      motorbikeFreeSpot()
      electricFreeSpot()
      showEmptySpotNumber()
    }
    class ParkingRate{
      hourNumber: int 
      rate: double
    }
    class ParkingSpot{
      number: string
      free: bool
      type: ParkingSlotType
      getlsFree(): bool
    }
    class EntrancePanel{
      id: string
      printTicket(): bool
    }

    class ExitPanel{
      id: string
      ScanTicket()
      processPayment()
    }

    class ParkingAttendantPortal{
      id : string
      scanTicket()
      processPayment()
    }

    class CustomerlinfoPortal{
      id: string
      scanTicket()
      processPayment()
    }

    class Vehicle{
      licenseNumber: string
      type: Vehicle 
      assignTicket()
    }
    class ParkingTicket{
      tocketNumber: string
      issuedAt: datetime
      payedAt: datetime
      payedAmount: double
      status: ParkingTicketStatus
    }

    class Car{
    }
    class Truck{
    }
    class Van{
    }
    class MoterBike{
    }
    class HandicappedSpot{
    }
    class CompactSpot{
    }
    class LargeSpot{
    }
    class MotorbikeSpot{
    }
    class ElectricSpot{
    }

    class Account{
      userName: string
      password: string
      status: AccountStatus
    }
    class ParkingAttendant{
      processTicket()
    }
    class Admin{
        AddParkingFloor()
    }


    ParkingLot *-- ParkingFloor
    ParkingLot *-- ParkingRate
    ParkingFloor *-- ParkingDisplayBoard 
    ParkingFloor *-- ParkingSpot
    ParkingFloor *-- CustomerlinfoPortal 
    ParkingLot *-- EntrancePanel 
    ParkingLot *-- ExitPanel 
    ParkingLot *-- ParkingAttendantPortal

    Vehicle --> ParkingTicket : has
    ParkingSpot --> Vehicle : has
    Car --|> Vehicle : Extends
    Truck --|> Vehicle : Extends
    Van --|> Vehicle : Extends
    MoterBike --|> Vehicle : Extends
    HandicappedSpot --|> ParkingSpot : Extends
    CompactSpot --|> ParkingSpot : Extends
    LargeSpot --|> ParkingSpot : Extends
    ElectricSpot --|> ParkingSpot : Extends
    MotorbikeSpot --|> ParkingSpot : Extends
    Admin --|> Account : Extends
    ParkingAttendant --|> Account : Extends
    ParkingAttendant --> ParkingTicket : process
            
```


### Activity diagram
------------
```mermaid

%%{init: { "theme": "forest","flowchart": {"nodeSpacing":10, "rankSpacing":20,"curve": "basic","useMaxWidth":true}} }%%
flowchart TD
    A[Start] --> B
    B(Customer inserts the parking ticket in the exit panel) --> C
    C(System scans the parking ticket and fetches ticket's details) --> D{{Ticket already paid ??}}
    E(System calculates the total parking fee)
    F(System shows the total parking fee on the display panel and ask for the credit card details)
    G(Customer inserts the credit card in the card reader)
    H(System reads the credit card details and processes the payment)
    I{{Payment Successtull ??}}
    J(system show the error)
    K{{Try again ??}}
    L(System shows success message)
    M{{Print receipt ??}}
    N(System prints  the receipt)
    O(Pay using cash)

    D -->|Yes| Y
    D --> |No| E --> F --> G --> H -->I
    I --> |No| J --> K
    K --> |Yes| G
    K --> |No| O --> L
    I --> |Yes|L --> M
    M -->|Yes| N --> Y
    M --> |No| Y
    Y(System send signal the signal to open parking gate) --> Z(End)
    
    classDef se fill:#FDFCFC, color:#283747,stroke:#6F6A68,stroke-width:2px
    classDef normal fill:#FDFCFC, color:#283747,stroke:#6F6A68,stroke-width:1px
    classDef question fill:#FDFCFC, color:#283747,stroke:#283747,stroke-width:1.5px,stroke-dasharray:3
    classDef success fill:#FDFCFC, color:#73C6B6,stroke:#283747
    classDef error fill:#FDFCFC, color:#EC7063 ,stroke:#283747
    class A,Z se
    class B,C,E,F,G,H,N,Y,O normal
    class D,I,M,K question
    class L success
    class J error
    linkStyle 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19 stroke:#6F6A68,stroke-width:1.2px,color:#6F6A68
 
 ```
 
### Code
------------

> ***Note => In below code the database implementation and payment implementation are skiped.***
 
 ###### Enums and Constants
 
  ```python
  from abc import ABC
from enum import Enum
from dataclasses import dataclass

class VehicleType(Enum):
    CAR, TRUCK, ELECTRIC, VAN, MOTORBIKE = 1, 2, 3, 4, 5

class ParkingSpotType(Enum):
    HANDICAPPED, COMPACT, LARGE, MOTORBIKE, ELECTRIC = 1, 2, 3, 4, 5

class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6

class ParkingTicketStatus(Enum):
    ACTIVE, PAID, LOST = 1, 2, 3

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
```
###### Account, Admin, and ParkingAttendant
```python
from dataclasses import dataclass

@dataclass
class Account(ABC):
    id: str
    password: str
    person: Person
    status: AccountStatus = AccountStatus.ACTIVE   

    def reset_password(self):
        None

@dataclass
class Admin(Account):
    def add_parking_floor(self, floor):
        None

    def add_parking_spot(self, floor_name, spot):
        None

    def add_parking_display_board(self, floor_name, display_board):
        None

    def add_customer_info_panel(self, floor_name, info_panel):
        None

    def add_entrance_panel(self, entrance_panel):
        None

    def add_exit_panel(self, exit_panel):
        None

@dataclass
class ParkingAttendant(Account):
    def process_ticket(self, ticket_number):
        None   
```
###### ParkingSpot
```python
from abc import ABC
from dataclasses import dataclass

@dataclass
class ParkingSpot(ABC):
    number: int
    parking_spot_type: ParkingSpotType
    free: bool = True
    vehicle: VehicleType = None

    def is_free(self):
        return self.__free

    def assign_vehicle(self, vehicle):
        self.__vehicle = vehicle
        free = False

    def remove_vehicle(self):
        self.__vehicle = None
        free = True

@dataclass
class HandicappedSpot(ParkingSpot):
    parking_spot_type: ParkingSpotType = ParkingSpotType.HANDICAPPED

class CompactSpot(ParkingSpot):
    parking_spot_type: ParkingSpotType = ParkingSpotType.COMPACT

class LargeSpot(ParkingSpot):
    parking_spot_type: ParkingSpotType = ParkingSpotType.LARGE

class MotorbikeSpot(ParkingSpot):
    parking_spot_type: ParkingSpotType = ParkingSpotType.MOTORBIKE

class ElectricSpot(ParkingSpot):
    parking_spot_type: ParkingSpotType = ParkingSpotType.ELECTRIC
```
###### ParkingTicket and Vehicle
```python
from abc import ABC , abstractmethod
from dataclasses import dataclass
import datetime

@dataclass
class ParkingTicket(ABC):
    token_number: str
    payedAt: datetime.date
    ammount: float
    status: ParkingTicketStatus
    issued_at: datetime.date = datetime.date.today()
    

@dataclass
class Vehicle(ABC):
    license_number: int
    vehicle_type: VehicleType
    ticket: ParkingTicket

    def assign_ticket(self, ticket):
        self.__ticket = ticket

@dataclass
class Car(Vehicle):
    VehicleType: VehicleType = VehicleType.CAR

@dataclass
class Van(Vehicle):
    VehicleType: VehicleType = VehicleType.VAN

@dataclass
class Truck(Vehicle):
    VehicleType: VehicleType = VehicleType.TRUCK
```

###### ParkingFloor and ParkingDisplayBoard
```python
from dataclasses import dataclass

@dataclass
class ParkingDisplayBoard:
    id: int
    handicapped_free_spot: int = None
    compact_free_spot: int = None
    large_free_spot: int = None
    motorbike_free_spot: int = None
    electric_free_spot: int = None

    def show_empty_spot_number(self):
        message = ""
        if self.__handicapped_free_spot.is_free():
            message += "Free Handicapped: " + self.__handicapped_free_spot.get_number()
        else:
            message += "Handicapped is full"
            message += "\n"

        if self.__compact_free_spot.is_free():
            message += "Free Compact: " + self.__compact_free_spot.get_number()
        else:
            message += "Compact is full"
            message += "\n"

        if self.__large_free_spot.is_free():
            message += "Free Large: " + self.__large_free_spot.get_number()
        else:
            message += "Large is full"
            message += "\n"

        if self.__motorbike_free_spot.is_free():
            message += "Free Motorbike: " + self.__motorbike_free_spot.get_number()
        else:
            message += "Motorbike is full"
            message += "\n"

        if self.__electric_free_spot.is_free():
            message += "Free Electric: " + self.__electric_free_spot.get_number()
        else:
            message += "Electric is full"

        print(message)

@dataclass
class ParkingFloor:
    name: str
    handicapped_spots: dict = {}
    compact_spots: dict = {}
    large_spots: dict = {}
    motorbike_spots: dict = {}
    electric_spots: dict = {}
    info_portals: dict = {}
    display_board: dict = {}

    def add_parking_spot(self, spot):
        switcher = {
        ParkingSpotType.HANDICAPPED: self.handicapped_spots.put(spot.get_number(), spot),
        ParkingSpotType.COMPACT: self.compact_spots.put(spot.get_number(), spot),
        ParkingSpotType.LARGE: self.large_spots.put(spot.get_number(), spot),
        ParkingSpotType.MOTORBIKE: self.motorbike_spots.put(spot.get_number(), spot),
        ParkingSpotType.ELECTRIC: self.electric_spots.put(spot.get_number(), spot),
        }
        switcher.get(spot.get_type(), 'Wrong parking spot type')

    def assign_vehicleToSpot(self, vehicle, spot):
        spot.assign_vehicle(vehicle)
        switcher = {
        ParkingSpotType.HANDICAPPED: self.update_display_board_for_handicapped(spot),
        ParkingSpotType.COMPACT: self.update_display_board_for_compact(spot),
        ParkingSpotType.LARGE: self.update_display_board_for_large(spot),
        ParkingSpotType.MOTORBIKE: self.update_display_board_for_motorbike(spot),
        ParkingSpotType.ELECTRIC: self.update_display_board_for_electric(spot),
        }
        switcher(spot.get_type(), 'Wrong parking spot type!')

    def update_display_board_for_handicapped(self, spot):
        if self.__display_board.get_handicapped_free_spot().get_number() == spot.get_number():
        # find another free handicapped parking and assign to display_board
            for key in self.__handicapped_spots:
                if self.__handicapped_spots.get(key).is_free():
                    self.__display_board.set_handicapped_free_spot(
                        self.__handicapped_spots.get(key))

            self.__display_board.show_empty_spot_number()

    def update_display_board_for_compact(self, spot):
        if self.__display_board.get_compact_free_spot().get_number() == spot.get_number():
        # find another free compact parking and assign to display_board
            for key in self.__compact_spots.key_set():
                if self.__compact_spots.get(key).is_free():
                    self.__display_board.set_compact_free_spot(
                        self.__compact_spots.get(key))

            self.__display_board.show_empty_spot_number()

    def free_spot(self, spot):
        spot.remove_vehicle()
        switcher = {
            ParkingSpotType.HANDICAPPED: self.update_free_handicapped_spot_count(),
            ParkingSpotType.COMPACT: self.update_free_compact_spot_count(),
            ParkingSpotType.LARGE: self.update_free_large_spot_count(),
            ParkingSpotType.MOTORBIKE: self.update_free_motorbike_spot_count(),
            ParkingSpotType.ELECTRIC: self.update_free_electric_spot_coun(),
        }
        switcher(spot.get_type(), 'Wrong parking spot type!')
```

###### ParkingLot
```python
from dataclasses import dataclass
import threading


@dataclass
class ParkingLot:
    name: str
    address: Address
    parking_rate: float
    lock: threading.Lock() 
    compact_spot_count: int = 0
    large_spot_count: int = 0
    motorbike_spot_count: int = 0
    electric_spot_count: int = 0
    max_compact_count: int = 0
    max_motorbike_count: int = 0
    entrance_panels: dict = {}
    exit_panels: dict = {}
    parking_floors: dict = {}


    def get_new_parking_ticket(self, vehicle):
        if self.is_full(vehicle.get_type()):
            raise Exception('Parking full!')
        # synchronizing to allow multiple entrances panels to issue a new
        # parking ticket without interfering with each other
        self.lock.acquire()
        ticket = ParkingTicket()
        vehicle.assign_ticket(ticket)
        ticket.save_in_DB()
        # if the ticket is successfully saved in the database, we can increment the parking spot count
        self.__increment_spot_count(vehicle.get_type())
        self.__active_tickets.put(ticket.get_ticket_number(), ticket)
        self.lock.release()
        return ticket

    def is_full(self, type):
        # trucks and vans can only be parked in LargeSpot
        if type == VehicleType.Truck or type == VehicleType.Van:
            return self.__large_spot_count >= self.__max_large_count

        # motorbikes can only be parked at motorbike spots
        if type == VehicleType.Motorbike:
            return self.__motorbike_spot_count >= self.__max_motorbike_count

        # cars can be parked at compact or large spots
        if type == VehicleType.Car:
            return (self.__compact_spot_count + self.__large_spot_count) >= (self.__max_compact_count + self.__max_large_count)

        # electric car can be parked at compact, large or electric spots
        return (self.__compact_spot_count + self.__large_spot_count + self.__electric_spot_count) >= (self.__max_compact_count + self.__max_large_count
                                                                                                    + self.__max_electric_count)

    # increment the parking spot count based on the vehicle type
    def increment_spot_count(self, type):
        if type == VehicleType.Truck or type == VehicleType.Van:
            large_spot_count += 1
        elif type == VehicleType.Motorbike:
            motorbike_spot_count += 1
        elif type == VehicleType.Car:
            if self.__compact_spot_count < self.__max_compact_count:
                compact_spot_count += 1
            else:
                large_spot_count += 1
        else:  # electric car
            if self.__electric_spot_count < self.__max_electric_count:
                electric_spot_count += 1
            elif self.__compact_spot_count < self.__max_compact_count:
                compact_spot_count += 1
            else:
                large_spot_count += 1

    def is_full(self):
        for key in self.__parking_floors:
            if not self.__parking_floors.get(key).is_full():
                return False
        return True

    def add_parking_floor(self, floor):
        # store in database
        None

    def add_entrance_panel(self, entrance_panel):
        # store in database
        None

    def add_exit_panel(self,  exit_panel):
        # store in database
        None

```
    
