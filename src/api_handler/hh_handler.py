from src.api_handler.abstract_handler import GeneralAPI


class HeadHunterAPI(GeneralAPI):
    """
        Класс для работы с API HeadHunter.

        Методы:
        --------
        get_vacancies
            Извлекает вакансии из API HeadHunter на основе ключевого слова.
    """
    url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, keyword):
        self.params = {
            'text': keyword,  # слово по которому ведется поиск
            'area': 1,  # Поиск в зоне
            'page': 1,  # Номер страницы
            'per_page': 10  # Кол-во вакансий на 1 странице
        }
        self.headers = {
            'User-Agent': 'MyImportantApp 1.0'
        }
        return self.send_request()
