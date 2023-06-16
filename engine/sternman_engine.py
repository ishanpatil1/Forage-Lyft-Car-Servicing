from engine.engine import Engine

class SternmanEngine(Engine):
    def needs_servicing(self,current_mileage,last_servicing_mileage,warning_light_on):
        return warning_light_on