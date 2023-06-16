from tire.tire import Tire

class OctoprimeTire(Tire):
    def needs_servicing(self, tire_wear):
        if tire_wear['tire_1'] + tire_wear['tire_2'] + tire_wear['tire_3'] + tire_wear['tire_4'] >= 3:
            return True