from tire.tire import Tire

class CarriganTire(Tire):
    def needs_servicing(self, tire_wear):
        if tire_wear['tire_1'] >= 0.9 or tire_wear['tire_2'] >= 0.9 or tire_wear['tire_3'] >= 0.9 or tire_wear['tire_4'] >= 0.9:
            return True