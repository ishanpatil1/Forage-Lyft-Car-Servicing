from engine.engine import Engine

class CapuletEngine(Engine):
    def needs_servicing(self,current_mileage,last_servicing_mileage):
        return current_mileage - last_servicing_mileage >=30000