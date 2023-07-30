from abc import ABC, abstractmethod


class JSONSaver(ABC):
    """
    Абстрактный базовый класс для сохранения и получения данных о вакансиях в формате JSON
    """
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def select_vacancy(self):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass
