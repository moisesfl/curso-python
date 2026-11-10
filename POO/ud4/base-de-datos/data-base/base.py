
from abc import ABC, abstractmethod

class Database(ABC):

    def __init__(self, database_name):
        self.database_name = database_name

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def read(self, record_id):
        pass

    @abstractmethod
    def update(self, record_id, data):
        pass

    @abstractmethod
    def delete(self, record_id):
        pass
