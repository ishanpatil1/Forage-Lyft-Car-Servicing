from engine.engine import Engine

class WilloughbyEngine(Engine):
    def needs_servicing(self,current_mileage,last_servicing_mileage):
        return current_mileage - last_servicing_mileage >=60000