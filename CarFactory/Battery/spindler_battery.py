from CarFactory.Battery.battery import Battery
import datetime


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self) -> bool:
        service_interval = 3
        # Spindler battery requires service after three years instead of two
        years_since_service = (self.current_date - self.last_service_date)/ 365
        
        if years_since_service >= service_interval:
            return True
        else:
            return False
