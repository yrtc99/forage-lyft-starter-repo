from CarFactory.Tires.tires import Tires

class Octoprime(Tires):
    def needs_service(self, tire_wear_array: list[float]) -> bool:
        if sum(tire_wear_array) >= 3:
            return True
        else:
            return False
