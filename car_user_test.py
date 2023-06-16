#This code is used to take inputs from user

import random

import unittest

import datetime

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.splinder_battery import SplinderBattery
from battery.nubbin_battery import NubbinBattery

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

from car.car import Car

class Servicing_test(unittest.TestCase):
    def test_need_service(self):

        #A loop added for the ability to add more variations to the values without rerunning the file
        redo="yes"
        while redo.lower()=="yes":
            engine_type=check_engine_type()
            battery_type=check_battery_type()
            tire_type=check_tire_type()
            last_servicing_date=check_last_servicing_date()
            current_mileage=check_current_mileage()
            last_servicing_mileage=check_last_servicing_mileage(current_mileage)
            warning_light_on=check_warning_light_on()
            tire_wear=check_tire_wear()

            #Here the values to be used will be printed
            print("\n\tThese values were selected\n","\n\t Engine Type:-",engine_type.__class__.__name__,"\n\t Battery Type:-",battery_type.__class__.__name__,
                  "\n\t Tire Type:-",tire_type.__class__.__name__, "\n\t Last Servicing Date:-",last_servicing_date,"\n\t Current Mileage:-",current_mileage,
                  "\n\t Last Servicing Mileage:-",last_servicing_mileage,"\n\t Warning light is on:-",warning_light_on,"\n\t Tire wear values:-",tire_wear)
            
            car1=Car(engine_type,battery_type,tire_type,last_servicing_date,current_mileage,last_servicing_mileage,warning_light_on,tire_wear)

            if car1.needs_servicing(datetime.datetime.today().date()):
                print("\n\t Your car needs servicing")
            else:
                print("\n\t No need for servicing")
            
            redo=input("Do you wish to continue (Yes/No):- ")

#These functions are responsible for user input
def check_engine_type():
    while True:
        engine_type=input("Enter the type of Engine in your car (CapuletEngine,SternmanEngine,WilloughbyEngine):- ")

        if engine_type.lower() == "capuletengine":
            return CapuletEngine()
        elif engine_type.lower() == "sternmanengine":
            return SternmanEngine()
        elif engine_type.lower() == "willoughbyengine":
            return WilloughbyEngine()
        else:
            print("\n Invalid engine type. ")

def check_battery_type():
    while True:
        battery_type=input("Enter the type of Battery in your car (SplinderBattery,NubbinBattery):- ")
    
        if battery_type.lower() == "splinderbattery":
            return SplinderBattery()
        elif battery_type.lower() == "nubbinbattery":
            return NubbinBattery()
        else:
            print("\n Invalid battery type. ")

def check_tire_type():
    while True:
        tire_type=input("Enter the type of Tires in your car (Carrigantire,Octoprimetire):- ")
    
        if tire_type.lower() == "carrigantire":
            return CarriganTire()
        elif tire_type.lower() == "octoprimetire":
            return OctoprimeTire()
        else:
            print("\n Invalid tire type. ")

def check_last_servicing_date():
    while True:
        last_servicing_date=input("Enter the last date of you car servicing (YYYY-MM-DD):- ")
        try:
            last_servicing_date = datetime.datetime.strptime(last_servicing_date, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date. ")
    
    return last_servicing_date 

def check_current_mileage():
    while True:
        current_mileage=int(input("Enter the current mileage of you car:- "))

        if isinstance(current_mileage, int):
            return current_mileage
        else:
            print("\n Invalid current mileage. ")

def check_last_servicing_mileage(current_mileage):
    while True:
        last_servicing_mileage=int(input("Enter the last servicing mileage of you car:- "))

        if isinstance(last_servicing_mileage, int) and last_servicing_mileage<current_mileage:
            return last_servicing_mileage
        else:
            print("\n Invalid previous servicing mileage")

def check_warning_light_on():
    while True:
        warning_light_on = input("Is the warning light of your car on? (True/False): ")

        if warning_light_on.lower() == "true":
            return True
        elif warning_light_on.lower() == "false":
            return False
        else:
            print("Invalid input. ")
            print("\n")

def check_tire_wear():
    while True:
        tire_wear= {
                'tire_1':float(input("Enter Tire 1 wear (0-1):-")),
                'tire_2':float(input("Enter Tire 2 wear (0-1):-")),
                'tire_3':float(input("Enter Tire 3 wear (0-1):-")),
                'tire_4':float(input("Enter Tire 4 wear (0-1):-"))
            }
        if all(isinstance(values,(float, int)) and 0 <= values <= 1 for values in tire_wear.values()):
            return tire_wear
        else:
            print("\n Invalid Tire wear value.")

if __name__=='__main__':
    unittest.main()