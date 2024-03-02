from CarFactory.Engine.engine import Engine 
from CarFactory.Battery.battery import Battery 
from CarFactory.Tires.tires import Tires
from CarFactory.serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tires: Tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()