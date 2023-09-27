from abc import ABC, abstractmethod
from enums import *
import datetime

class ParkingTicket(ABC):
    def __init__(self,token):
        self.token= token
        self.ammount =  0
        self.issued_at = datetime.datetime.now()
        self.payed = False
        self.payedAt= None


class ParkingLot(ABC):

    def __init__(self,name,location):
        self.name=name
        self.location=location


    def addVehicleToSpot(self, spot, vehicle):
        parkingTicket = None
        token = spot.assign_vehicle(vehicle)
        if token != "OutOfCapcity":
            parkingTicket = ParkingTicket(token)
        return parkingTicket
    
    def removeVehicleFromSpot(self, spot, ticket):
        spot.remove_vehicle(ticket.token)
        now = datetime.datetime.now()
        duration = now - ticket.issued_at
        duration_in_s = duration.total_seconds() 
        hours= duration_in_s / 3600
        # hours = divmod(duration_in_s, 3600)[0]
        return spot.pricingModel.calculate_price(hours)
      
        
        

    @abstractmethod
    def park_vehicle(self, vehicle):
        pass

    @abstractmethod
    def unpark_vehicle(self, vehicle):
        pass

    @abstractmethod
    def add_moter_bike_parking_spot(self, spot):
        pass

    @abstractmethod
    def add_car_parking_spot(self, spot):
        pass

    @abstractmethod
    def add_truck_parking_spot(self, spot):
        pass
    

class MallParkingLot(ParkingLot):
    def __init__(self,name,location):
        super().__init__(name, location)
    
    def add_moter_bike_parking_spot(self, spot):
        self.moter_bike_spots = spot

    def add_car_parking_spot(self, spot):
        self.car_spots = spot

    def add_truck_parking_spot(self, spot):
        self.truck_sports = spot

    def park_vehicle(self, vehicle):
        switcher = {
        VehicleType.MOTORBIKE: self.addVehicleToSpot(self.moter_bike_spots, vehicle),
        VehicleType.CAR: self.addVehicleToSpot(self.car_spots, vehicle),
        VehicleType.TRUCK: self.addVehicleToSpot(self.truck_sports, vehicle),
        }
        ticket = switcher.get(vehicle.vehical_type, lambda: 'Wrong vehicle type!')
        if ticket is None :
            return "No Space Available"
        return ticket

    def unpark_vehicle(self, vehicle, ticket):
        switcher = {
        VehicleType.MOTORBIKE: self.removeVehicleFromSpot(self.moter_bike_spots, ticket),
        VehicleType.CAR: self.removeVehicleFromSpot(self.car_spots, ticket),
        VehicleType.TRUCK: self.removeVehicleFromSpot(self.truck_sports, ticket),
        }
        price = switcher.get(vehicle.vehical_type, lambda: 'Wrong vehicle type!')
        return price   

class StadiumParkingLot(ParkingLot):
    def __init__(self,name,location):
        super().__init__(name, location)
    
    def add_moter_bike_parking_spot(self, spot):
        self.moter_bike_spots = spot

    def add_car_parking_spot(self, spot):
        self.car_spots = spot

    def add_truck_parking_spot(self, spot):
        return "not supported"
    
    def park_vehicle(self, vehicle):
        switcher = {
        VehicleType.MOTORBIKE: self.addVehicleToSpot(self.moter_bike_spots, vehicle),
        VehicleType.CAR: self.addVehicleToSpot(self.car_spots, vehicle),
        VehicleType.TRUCK: "Not Supported",
        }
        ticket = switcher.get(vehicle.vehical_type, lambda: 'Wrong vehicle type!')
        if ticket is None :
            return "No Space Available"
        return ticket

    def unpark_vehicle(self, vehicle, ticket):
        switcher = {
        VehicleType.MOTORBIKE: self.removeVehicleFromSpot(self.moter_bike_spots, ticket),
        VehicleType.CAR: self.removeVehicleFromSpot(self.car_spots, ticket),
        VehicleType.TRUCK: "Not Supported",
        }
        price = switcher.get(vehicle.vehical_type, lambda: 'Wrong vehicle type!')
        return price

class AirportParkingLot(ParkingLot):
    def __init__(self,name,location):
        super().__init__(name, location)
    
    def add_moter_bike_parking_spot(self, spot):
        self.moter_bike_spots = spot

    def add_car_parking_spot(self, spot):
        self.car_spots = spot

    def add_truck_parking_spot(self, spot):
        return "not supported"
    
    def park_vehicle(self, vehicle):
        switcher = {
        VehicleType.MOTORBIKE: self.addVehicleToSpot(self.moter_bike_spots, vehicle),
        VehicleType.CAR: self.addVehicleToSpot(self.car_spots, vehicle),
        VehicleType.TRUCK: "Not Supported",
        }
        ticket = switcher.get(vehicle.vehical_type, lambda: 'Wrong vehicle type!')
        if ticket is None :
            return "No Space Available"
        return ticket

    def unpark_vehicle(self, vehicle, ticket):
        switcher = {
        VehicleType.MOTORBIKE: self.removeVehicleFromSpot(self.moter_bike_spots, ticket),
        VehicleType.CAR: self.removeVehicleFromSpot(self.car_spots, ticket),
        VehicleType.TRUCK: "Not Supported",
        }
        price = switcher.get(vehicle.vehical_type, lambda: 'Wrong vehicle type!')
        return price