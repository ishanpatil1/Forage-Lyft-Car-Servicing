from abc import ABC,abstractmethod

class Engine(ABC):
    @abstractmethod
    def needs_servicing(self,current_mileage,last_servicing_mileage):
        pass