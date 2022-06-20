
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

    ParkingLot *-- ParkingFloor
    ParkingFloor *-- ParkingDisplayBoard  

```
