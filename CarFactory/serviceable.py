from abc import ABC, abstractmethod


# Interface for parts that need servicing
class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass