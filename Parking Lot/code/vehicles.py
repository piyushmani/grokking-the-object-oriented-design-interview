from abc import ABC, abstractmethod
from enums import *


class Vehicle(ABC):
    def __init__(self,license_number):
        self.license_number = license_number
        self.parking_ticket = None

    def assign_ticket(self, ticket):
        self.parking_ticket = ticket 

class MoterBike(Vehicle):
    def __init__(self,license_number):
        super().__init__(license_number)
        self.vehical_type = VehicleType.MOTORBIKE


class Car(Vehicle):
    def __init__(self,license_number):
        super().__init__(license_number)
        self.vehical_type = VehicleType.CAR

class Truck(Vehicle):
    def __init__(self,license_number):
        super().__init__(license_number)
        self.vehical_type = VehicleType.TRUCK 