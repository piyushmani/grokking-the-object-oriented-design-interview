from abc import ABC, abstractmethod
from abc import ABCMeta, abstractmethod
import math
import datetime
from enums import *

class Rate(metaclass=ABCMeta):
    @abstractmethod
    def calculate_price(self):
        pass

class FlatRate(Rate):

    def __init__(self,rate):
        """
        Parameters
        ----------
        rate : float
            price based on per hour
        
        """
        self.rate = rate

    def calculate_price(self, hour):
        return self.rate*hour 
    

class DynamicRate(Rate):

    def __init__(self,interval_rates,dynamic_rate):
        """
        Parameters
        ----------
        interval_rates : tupple
            price for different time interval in form for tupple ex: (("0-4",30),("4-12",60))
        dynamic_rate : tupple
            price after fixed interval has crossed ex: (RateType.PER_HOUR, 100 )
        """

        self.interval_rates = interval_rates
        self.dynamic_rate = dynamic_rate

    def calculate_price(self, hours):
        price = 0
        
        if self.dynamic_rate[0] == RateType.PER_HOUR:
            for rate in self.interval_rates:
                if hours > 0:
                    range = rate[0].split("-")
                    total_hour_in_range = float(range[1])-float(range[0])
                    price+=rate[1]
                    hours-=total_hour_in_range
                else:
                    break 
            hours=  math.ceil(hours) 
                 
            if hours > 0 :
                price += hours*self.dynamic_rate[1]

        else:
            if hours >= 24 :
                days = math.ceil(hours/24)
                return days*self.dynamic_rate[1]
            
            else:
                for rate in self.interval_rates:
                    range = rate[0].split("-")
                    if  float(range[0]) <= hours <= float(range[1]):
                        price=rate[1]
                        return price
                     
        return price 