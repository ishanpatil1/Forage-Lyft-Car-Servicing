from engine.engine import Engine
from battery.battery import Battery
from tire.tire import Tire
from datetime import datetime

class Car:
    def __init__(self,engine: Engine, battery: Battery, tire: Tire, last_servicing_date: datetime, current_mileage: int, last_servicing_mileage: int, warning_light_on: bool, tire_wear: dict):
        self.engine = engine
        self.battery = battery
        self.tire=tire
        self.last_servicing_date = last_servicing_date
        self.current_mileage= current_mileage
        self.last_servicing_mileage= last_servicing_mileage
        self.warning_light_on= warning_light_on
        self.tire_wear=tire_wear

        #Initial values for the tire_wear dict
        tire_wear = {
            'tire_1':0, 
            'tire_2':0,
            'tire_3':0,
            'tire_4':0,
            }
    
    def needs_servicing(self,current_date: datetime):
        if( self.engine.needs_servicing(self.current_mileage,self.last_servicing_mileage,self.warning_light_on) 
           or self.battery.needs_servicing(self.last_servicing_date,current_date)
           or self.tire.needs_servicing(self.tire_wear)):
            return True
        else:
            return False