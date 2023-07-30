from src.api_handler.abstract_handler import GeneralAPI


class SuperJobAPI(GeneralAPI):
    """
        Класс для работы с API SuperJob.

        Методы:
        --------
        get_vacancies
            Извлекает вакансии из API SuperJob на основе ключевого слова.
    """
    url = 'https://api.superjob.ru/2.0/vacancies/'

    def get_vacancies(self, keyword):
        self.params = {
            'keyword': keyword,  # слово по которому ведется поиск
            'count': 10,  # Кол-во вакансий на 1 странице
            'page': None  # Номер страницы
        }
        self.headers = {
            'X-Api-App-Id': 'v3.r.137690466.c764484ba4cf010925762af5b315a1e5cf662801.12cf31efd3e3ebff4ecb9b5008dcd35b97fb634a'
        }
        return self.send_request()
