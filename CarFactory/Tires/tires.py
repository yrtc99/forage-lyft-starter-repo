from CarFactory.serviceable import Serviceable, abstractmethod

class Tires(Serviceable):

    def __init__(self, tire_wear_array: list[float]):
        self.tire_wear_array = tire_wear_array
   
    def needs_service(self) -> bool:
        pass