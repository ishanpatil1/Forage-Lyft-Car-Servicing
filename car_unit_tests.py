#This code is used to perform unit tests on the code

import unittest
import random
import datetime
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.splinder_battery import SplinderBattery
from battery.nubbin_battery import NubbinBattery
from car.car import Car

class ServicingTest(unittest.TestCase):
    def test_need_service(self):
        for i in range(50): #You can change the amount of tests it may run by changing the value in the range() function
            engine_type = random.choice([CapuletEngine(), WilloughbyEngine(), SternmanEngine()])
            battery_type = random.choice([SplinderBattery(), NubbinBattery()])
            last_servicing_date = datetime.datetime.now().date() - datetime.timedelta(days=random.randint(1, 2000))
            current_mileage = random.randint(0, 100000)
            last_servicing_mileage = random.randint(0, current_mileage)
            warning_light_on = random.choice([True, False])
            
            car1 = Car(engine_type, battery_type, last_servicing_date, current_mileage, last_servicing_mileage, warning_light_on)
            needs_servicing=car1.needs_servicing(datetime.datetime.today().date())

            print("\n\tThese values were selected\n","\n\t",engine_type.__class__.__name__,"\n\t",battery_type.__class__.__name__,
                  "\n\t",last_servicing_date,"\n\t",current_mileage,"\n\t",last_servicing_mileage,"\n\t",warning_light_on)

            if car1.needs_servicing(datetime.datetime.today().date()):
                # self.assertTrue(car1.needs_servicing(datetime.datetime.today().date()), "No need of servicing")
                print("\n\t Your car needs servicing")
            else:
                #self.assertFalse(car1.needs_servicing(datetime.datetime.today().date()), "Needs servicing")
                print("\n\t No need for servicing")
        
        #self.assertTrue(car1.needs_servicing(datetime.datetime.today().date()))
        self.assertTrue(needs_servicing)

if __name__ == '__main__':
    unittest.main()