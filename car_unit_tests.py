#This code is used to perform unit tests on the code

import unittest
import random
import datetime
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.splinder_battery import SplinderBattery
from battery.nubbin_battery import NubbinBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire
from car.car import Car

class ServicingTest(unittest.TestCase):
    def test_need_service(self):
        for i in range(50): #You can change the amount of tests it may run by changing the value in the range() function
            engine_type = random.choice([CapuletEngine(), WilloughbyEngine(), SternmanEngine()])
            battery_type = random.choice([SplinderBattery(), NubbinBattery()])
            tire_type= random.choice([CarriganTire(),OctoprimeTire()])
            last_servicing_date = datetime.datetime.now().date() - datetime.timedelta(days=random.randint(1, 2500))
            current_mileage = random.randint(0, 100000)
            last_servicing_mileage = random.randint(0, current_mileage)
            warning_light_on = random.choice([True, False])
            tire_wear= {
                ('tire_1'):round(random.random(),1),
                ('tire_2'):round(random.random(),1),
                ('tire_3'):round(random.random(),1),
                ('tire_4'):round(random.random(),1)
            }
            
            car1 = Car(engine_type, battery_type, tire_type, last_servicing_date, current_mileage, last_servicing_mileage, warning_light_on, tire_wear)

            print("\n\tThese values were selected\n","\n\t Engine Type:-",engine_type.__class__.__name__,"\n\t Battery Type:-",battery_type.__class__.__name__,
                  "\n\t Tire Type:-",tire_type.__class__.__name__, "\n\t Last Servicing Date:-",last_servicing_date,"\n\t Current Mileage:-",current_mileage,
                  "\n\t Last Servicing Mileage:-",last_servicing_mileage,"\n\t Warning light is on:-",warning_light_on,"\n\t Tire wear values:-",tire_wear)

            if car1.needs_servicing(datetime.datetime.today().date()):
                self.assertTrue(car1.needs_servicing(datetime.datetime.today().date()), "No need of servicing")
                print("\n\t Your car needs servicing")
            else:
                self.assertFalse(car1.needs_servicing(datetime.datetime.today().date()), "Needs servicing")
                print("\n\t No need for servicing")

if __name__ == '__main__':
    unittest.main()