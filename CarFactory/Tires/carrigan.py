from CarFactory.Tires.tires import Tires

class Carrigan(Tires):
    def needs_service(self, tire_wear_array: list[float]) -> bool:
        for tire in tire_wear_array:
            if tire >= 0.9:
                return True
        return False