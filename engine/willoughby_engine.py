<<<<<<< HEAD
from engine.engine import Engine

class WilloughbyEngine(Engine):
    def __init__(self, current_mileage: int, last_service_mileage: int):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
=======
from abc import ABC

from car import Car


class WilloughbyEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
>>>>>>> 1c26f9cbad7b9bf859b3de73c4c65fb58e028a5f
        return self.current_mileage - self.last_service_mileage > 60000
