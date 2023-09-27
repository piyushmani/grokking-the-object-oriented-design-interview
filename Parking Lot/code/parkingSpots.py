from abc import ABC, abstractmethod
from enums import *

class ParkingSpot(ABC):
    def __init__(self,capcity):
        self.capcity = capcity
        self.spots={"%.3d" % num: None for num in range(self.capcity)}

    def is_free(self):
        return self.capcity > 0

    def assign_vehicle(self, vehicle):
        if self.is_free():
            for key,val in self.spots.items():
                if val is None :
                    self.spots[key]= vehicle
                    self.capcity=self.capcity-1
                    return key
        else:
            return "OutOfCapcity"            
        

    def remove_vehicle(self, ticket):
        self.spots[ticket]=None
        self.capcity+=1    

class MoterBikeSpot(ParkingSpot):
    def __init__(self,capcity, pricingModel):
        super().__init__(capcity)
        self.parking_type = VehicleType.MOTORBIKE
        self.pricingModel = pricingModel

class CarParkingSpot(ParkingSpot):
    def __init__(self,capcity,pricingModel):
        super().__init__(capcity)
        self.parking_type = VehicleType.CAR
        self.pricingModel = pricingModel

class TruckParkingSpot(ParkingSpot):
    def __init__(self,capcity,pricingModel):
        super().__init__(capcity)
        self.parking_type = VehicleType.TRUCK
        self.pricingModel = pricingModel