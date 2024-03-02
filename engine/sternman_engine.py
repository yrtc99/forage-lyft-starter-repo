<<<<<<< HEAD
from engine.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on: bool):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
=======
from abc import ABC

from car import Car


class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
>>>>>>> 1c26f9cbad7b9bf859b3de73c4c65fb58e028a5f
        if self.warning_light_is_on:
            return True
        else:
            return False
