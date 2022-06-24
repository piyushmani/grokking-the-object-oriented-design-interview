
**Table of Contents**

- [System Requirements](https://github.com/piyushmani/object-oriented-design-python/tree/main/Library%20Management%20System#system-requirements)
- [Use case diagram](https://github.com/piyushmani/object-oriented-design-python/tree/main/Library%20Management%20System#use-case-diagram)
- [Class diagram](https://github.com/piyushmani/object-oriented-design-python/tree/main/Library%20Management%20System#class-diagram)
- [Activity diagrams](https://github.com/piyushmani/object-oriented-design-python/tree/main/Library%20Management%20System#activity-diagrams)
- [Code](https://github.com/piyushmani/object-oriented-design-python/tree/main/Library%20Management%20System#code)

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
    C(System scans the parking ticket and fetches ticket's details) --> D{{ fa:fa-twitter Ticket already paid ??}}
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
 
 ```
    
