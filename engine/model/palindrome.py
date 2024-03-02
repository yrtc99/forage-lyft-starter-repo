from datetime import datetime

from engine.sternman_engine import SternmanEngine


class Palindrome(SternmanEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.needs_service():
            return True
        else:
            return False
