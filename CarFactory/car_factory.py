from CarFactory.car import Car
from CarFactory.Engine.capulet_engine import CapuletEngine
from CarFactory.Engine.sternman_engine import SternmanEngine
from CarFactory.Engine.willoughby_engine import WilloughbyEngine
from CarFactory.Battery.battery import Battery
from CarFactory.Battery.nubbin_battery import NubbinBattery
from CarFactory.Battery.spindler_battery import SpindlerBattery
from CarFactory.Tires.tires import Tires
from datetime import date

class CarFactory:
    
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_array: list[float]) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = Tires(tire_wear_array)
        return Car(engine, battery, tire)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_array: list[float]) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = Tires(tire_wear_array)
        return Car(engine, battery, tire)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool, tire_wear_array: list[float]) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = NubbinBattery(last_service_date, current_date)
        tire = Tires(tire_wear_array)
        return Car(engine, battery, tire)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_array: list[float]) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = Tires(tire_wear_array)
        return Car(engine, battery, tire)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_array: list[float]) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = Tires(tire_wear_array)
        return Car(engine, battery, tire)