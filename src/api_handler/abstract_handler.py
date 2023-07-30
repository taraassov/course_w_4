from abc import ABC, abstractmethod
import requests


class GeneralAPI(ABC):
    """
    Абстрактный базовый класс для работы с API
    """
    url = None
    params = None
    headers = None

    @abstractmethod
    def get_vacancies(self, keyword):
        pass

    def send_request(self):
        response = requests.get(
            self.url,
            params=self.params,
            headers=self.headers
        )

        # обработка ответа API
        return response.json()
