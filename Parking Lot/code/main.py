from enums import *
from rates import FlatRate, DynamicRate
from vehicles import MoterBike,  Car, Truck
from parkingSpots import MoterBikeSpot, CarParkingSpot, TruckParkingSpot
from parkingLots import MallParkingLot, AirportParkingLot 


def main():
    fkat_rate= FlatRate(10)
    interval_rates=(("0-4",30),("4-12",60))
    interval_rates=(("0-1",0),("1-8",40), ("8-60",40))
    per_hour_rates=(RateType.PER_HOUR, 100 )
    per_day_rates=(RateType.PER_DAY, 100 )
    dy__rate= DynamicRate(interval_rates, per_hour_rates)

    moterBike = MoterBike("123")

    res= dy__rate.calculate_price(43.05)
    

    moterBike = MoterBike("123")
    car = Car("car_123")
    truck = Truck("truck_123")
    

    spot = MoterBikeSpot(100, dy__rate)
    carspots = CarParkingSpot(100, dy__rate)
    mall_parking  = AirportParkingLot("Airport", "noida")
    mall_parking.add_moter_bike_parking_spot(spot)
    mall_parking.add_car_parking_spot(carspots)
    ticket = mall_parking.park_vehicle(moterBike)
    mall_parking.unpark_vehicle(moterBike, ticket)
            
if __name__ == '__main__':
    main()