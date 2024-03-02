import unittest
from datetime import date
from CarFactory.car_factory import CarFactory

class TestCarFactory(unittest.TestCase):
    def test_create_calliope(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 10000
        last_service_mileage = 5000

        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertIsNotNone(car)
        # Add additional assertions for the created car

    def test_create_glissade(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 20000
        last_service_mileage = 10000

        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertIsNotNone(car)
        # Add additional assertions for the created car

    def test_create_palindrome(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year - 1)
        warning_light_on = True

        car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_on)
        self.assertIsNotNone(car)
        # Add additional assertions for the created car

    def test_create_rorschach(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 30000
        last_service_mileage = 15000

        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertIsNotNone(car)
        # Add additional assertions for the created car

    def test_create_thovex(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 40000
        last_service_mileage = 20000

        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertIsNotNone(car)
        # Add additional assertions for the created car

if __name__ == '__main__':
    unittest.main()