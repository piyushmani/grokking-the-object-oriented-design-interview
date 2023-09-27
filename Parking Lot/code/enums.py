from enum import Enum

class VehicleType(Enum):
    MOTORBIKE, CAR, TRUCK, = 1, 2, 3

class RateType(Enum):
    PER_HOUR, PER_DAY, = 1, 2  

class ParkingLotType(Enum):
    MALL, STADIUM, AIRPORT = 1, 2 ,3