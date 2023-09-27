import unittest
from datetime import datetime, timedelta

from enums import *
from rates import FlatRate, DynamicRate
from vehicles import MoterBike,  Car, Truck
from parkingSpots import MoterBikeSpot, CarParkingSpot, TruckParkingSpot
from parkingLots import MallParkingLot, AirportParkingLot, StadiumParkingLot, ParkingTicket



class TestRateCalculations(unittest.TestCase):

    def test_flat_rate(self):
        flat_rate = FlatRate(10)
        self.assertEqual(flat_rate.calculate_price(20) , 200)

    def test_dynamic_rate_per_hour(self):
        interval_rates=(("0-4",30),("4-12",60))
        per_hour_rates=(RateType.PER_HOUR, 100 )
        dynamc_per_hour = DynamicRate(interval_rates, per_hour_rates)
        self.assertEqual(dynamc_per_hour.calculate_price(15) , 390)

    def test_dynamic_rate_per_day(self):
        interval_rates=(("0-1",0),("1-8",40), ("8-60",40))
        per_day_rates=(RateType.PER_DAY, 100 )
        dynamc_per_day = DynamicRate(interval_rates, per_day_rates)
        self.assertEqual(dynamc_per_day.calculate_price(25) , 200)  

class TestMallParkingLots(unittest.TestCase): 
    def setUp(self) -> None:
        self.moterBike_1 = MoterBike("moterbike_001")
        self.moterBike_2 = MoterBike("moterbike_002")
        self.moterBike_3 = MoterBike("moterbike_003")
        self.car_1 = Car("car_001")
        self.car_2 = Car("car_002")
        self.truck_1 = Truck("truck_001")
        self.truck_2 = Truck("truck_001")

        self.flat_rate_for_moterbike = FlatRate(10)
        self.flat_rate_for_car = FlatRate(20)
        self.flat_rate_for_truck = FlatRate(50)

        self.moterbike_spot = MoterBikeSpot(2,  self.flat_rate_for_moterbike)
        self.car_spot = CarParkingSpot(5,  self.flat_rate_for_car)
        self.truck_spot = TruckParkingSpot(3,  self.flat_rate_for_truck)

        self.parking_lot = MallParkingLot("supper Mall", "noida")  

        self.parking_lot.add_moter_bike_parking_spot(self.moterbike_spot)
        self.parking_lot.add_car_parking_spot(self.car_spot)  
        self.parking_lot.add_truck_parking_spot(self.truck_spot)

    def test_moterbike_park(self):
        res= self.parking_lot.park_vehicle(self.moterBike_1)
        self.assertIsInstance(res , ParkingTicket)

    def test_another_moterbike_park(self):
        res= self.parking_lot.park_vehicle(self.moterBike_2)
        self.assertIsInstance(res , ParkingTicket)

    def test_failed_moterbike_park(self):
        self.parking_lot.park_vehicle(self.moterBike_3)
        self.parking_lot.park_vehicle(self.moterBike_3)
        res = self.parking_lot.park_vehicle(self.moterBike_3)
        self.assertEqual(res , "No Space Available")     

    def test_moterbike_unpark(self):
        ticket= self.parking_lot.park_vehicle(self.moterBike_1)
        ticket.issued_at  = datetime.now() - timedelta(hours = 10)
        price = self.parking_lot.unpark_vehicle(self.moterBike_1, ticket)
        self.assertEqual(price , 100)

    def test_car_park_unpark(self):
        ticket= self.parking_lot.park_vehicle(self.car_1)
        ticket.issued_at  = datetime.now() - timedelta(hours = 5)
        price = self.parking_lot.unpark_vehicle(self.car_1, ticket)
        self.assertEqual(price , 100) 

    def test_truck_park_unpark(self):
        ticket= self.parking_lot.park_vehicle(self.truck_1)
        ticket.issued_at  = datetime.now() - timedelta(hours = 50)
        price = self.parking_lot.unpark_vehicle(self.truck_1, ticket)
        self.assertEqual(price , 2500)               



class TestAirportParkingLots(unittest.TestCase): 
    def setUp(self) -> None:
        self.moterBike_1 = MoterBike("moterbike_001")
        self.moterBike_2 = MoterBike("moterbike_002")
        self.moterBike_3 = MoterBike("moterbike_003")
        self.car_1 = Car("car_001")
        self.car_2 = Car("car_002")
        self.truck_1 = Truck("truck_001")

        self.interval_rat_for_moterbike = (("0-1",0),("1-8",40), ("8-24",60))
        self.interval_rat_for_car = (("0-12",60),("12-24",80))
        self.dynamic_rat_for_moterbike = (RateType.PER_DAY, 80 )
        self.dynamic_rat_for_car = (RateType.PER_DAY, 100 )

        self.rate_for_moterbike = DynamicRate(self.interval_rat_for_moterbike,self.dynamic_rat_for_moterbike )
        self.rate_for_car = DynamicRate(self.interval_rat_for_car,self.dynamic_rat_for_car )

        self.moterbike_spot = MoterBikeSpot(20,  self.rate_for_moterbike)
        self.car_spot = CarParkingSpot(50,  self.rate_for_car)

        self.parking_lot = AirportParkingLot("IGI Airport", "delhi")  

        self.parking_lot.add_moter_bike_parking_spot(self.moterbike_spot)
        self.parking_lot.add_car_parking_spot(self.car_spot)  

    def test_airport_moterbike_park(self):
        res= self.parking_lot.park_vehicle(self.moterBike_1)
        self.assertIsInstance(res , ParkingTicket)   

    def test_airport_moterbike_unpark(self):
        ticket= self.parking_lot.park_vehicle(self.moterBike_1)
        ticket.issued_at  = datetime.now() - timedelta(hours = 15)
        price = self.parking_lot.unpark_vehicle(self.moterBike_1, ticket)
        self.assertEqual(price , 60)

    def test_car_park_unpark(self):
        ticket= self.parking_lot.park_vehicle(self.car_1)
        ticket.issued_at  = datetime.now() - timedelta(hours = 23.9)
        price = self.parking_lot.unpark_vehicle(self.car_1, ticket)
        self.assertEqual(price , 80)

    def test_car_park_unpark_for_more_than_day(self):
        ticket= self.parking_lot.park_vehicle(self.car_1)
        ticket.issued_at  = datetime.now() - timedelta(hours = 40)
        price = self.parking_lot.unpark_vehicle(self.car_1, ticket)
        self.assertEqual(price , 200)     

    def test_failed_truck_park(self):
        ticket= self.parking_lot.park_vehicle(self.truck_1)
        self.assertEqual(ticket , "Not Supported")               
     
class TestStadiumParkingLots(unittest.TestCase): 
    def setUp(self) -> None:
        self.moterBike_1 = MoterBike("moterbike_001")
        self.moterBike_2 = MoterBike("moterbike_002")
        self.moterBike_3 = MoterBike("moterbike_003")
        self.car_1 = Car("car_001")
        self.car_2 = Car("car_002")
        self.truck_1 = Truck("truck_001")

        self.interval_rat_for_moterbike = (("0-4",30),("4-12",60))
        self.interval_rat_for_car = (("0-4",60),("4-12",120))
        self.dynamic_rat_for_moterbike = (RateType.PER_HOUR, 100 )
        self.dynamic_rat_for_car = (RateType.PER_HOUR, 200 )

        self.rate_for_moterbike = DynamicRate(self.interval_rat_for_moterbike,self.dynamic_rat_for_moterbike )
        self.rate_for_car = DynamicRate(self.interval_rat_for_car,self.dynamic_rat_for_car )

        self.moterbike_spot = MoterBikeSpot(20,  self.rate_for_moterbike)
        self.car_spot = CarParkingSpot(50,  self.rate_for_car)

        self.parking_lot = StadiumParkingLot("GreenPark", "delhi")  

        self.parking_lot.add_moter_bike_parking_spot(self.moterbike_spot)
        self.parking_lot.add_car_parking_spot(self.car_spot)  

    def test_stadium_moterbike_park(self):
        res= self.parking_lot.park_vehicle(self.moterBike_1)
        self.assertIsInstance(res , ParkingTicket)   

    def test_stadium_moterbike_unpark(self):
        ticket= self.parking_lot.park_vehicle(self.moterBike_1)
        ticket.issued_at  = datetime.now() - timedelta(hours = 3.6)
        price = self.parking_lot.unpark_vehicle(self.moterBike_1, ticket)
        self.assertEqual(price , 30)

    def test_stadium_car_park_unpark(self):
        ticket= self.parking_lot.park_vehicle(self.car_1)
        ticket.issued_at  = datetime.now() - timedelta(hours = 11.5)
        price = self.parking_lot.unpark_vehicle(self.car_1, ticket)
        self.assertEqual(price , 180)

    def test_stadium_car_park_unpark_for_more_than_12_hour(self):
        ticket= self.parking_lot.park_vehicle(self.car_1)
        ticket.issued_at  = datetime.now() - timedelta(hours = 13.5)
        price = self.parking_lot.unpark_vehicle(self.car_1, ticket)
        self.assertEqual(price , 580)     

    def test_failed_truck_park_in_stadium(self):
        ticket= self.parking_lot.park_vehicle(self.truck_1)
        self.assertEqual(ticket , "Not Supported")

        

if __name__ == '__main__':
    unittest.main()        