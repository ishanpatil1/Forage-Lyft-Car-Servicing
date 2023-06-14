from engine.engine import Engine
from battery.battery import Battery
from datetime import datetime

class Car:
    def __init__(self,engine: Engine, battery: Battery, last_servicing_date: datetime, current_mileage: int, last_servicing_mileage: int, warning_light_on: bool):
        self.engine = engine
        self.battery = battery
        self.last_servicing_date = last_servicing_date
        self.current_mileage= current_mileage
        self.last_servicing_mileage= last_servicing_mileage
        self.warning_light_on= warning_light_on
    
    def needs_servicing(self,current_date: datetime):
        if( self.engine.needs_servicing(self.current_mileage,self.last_servicing_mileage) 
           or self.battery.needs_servicing(self.last_servicing_date,current_date)
           or self.warning_light_on):
            return True
        else:
            return False