from abc import ABC,abstractmethod

class Tire(ABC):
    @abstractmethod
    def needs_servicing(self,tire_wear):
        pass