from abc import ABC,abstractmethod

class Battery(ABC):
    @abstractmethod
    def needs_servicing(self, last_servicing_date, current_date):
        pass