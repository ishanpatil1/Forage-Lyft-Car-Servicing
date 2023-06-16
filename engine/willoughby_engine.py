from engine.engine import Engine

class WilloughbyEngine(Engine):
    def needs_servicing(self,current_mileage,last_servicing_mileage,warning_light_on):
        return current_mileage - last_servicing_mileage >=60000