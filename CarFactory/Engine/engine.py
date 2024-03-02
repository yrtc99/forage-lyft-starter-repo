from abc import ABC
from car import Car
from CarFactory.serviceable import Serviceable

class Engine(Serviceable):
    def needs_service(self) -> bool:
        pass