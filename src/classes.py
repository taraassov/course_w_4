class VacancyAPI:
    """
        Класс для получения вакансий из API HeadHunter и SuperJobAPI.

        Методы:
        --------
        get_vacancies
            Извлекает вакансии из HeadHunterAPI и SuperJobAPI на основе ключевого слова.
    """

    def __init__(self, hh_api, sj_api):
        self.hh_api = hh_api
        self.sj_api = sj_api

    def get_vacancies(self, keyword):
        hh_vacancies = self.hh_api.get_vacancies(keyword)
        sj_vacancies = self.sj_api.get_vacancies(keyword)

        hh_vacancies_list = [
            {
                'title': item['name'],
                'company': item['employer']['name'],
                'salary': item['salary'],
                'link': item['alternate_url'],
                'source': 'hh'
            }
            for item in hh_vacancies['items']
        ]

        sj_vacancies_list = [
            {
                'title': item['profession'],
                'company': item.get('company_name'),  # get() для возврата None, если ключ не существует
                'salary': item['payment_from'],
                'link': item['link'],
                'source': 'sj'
            }
            for item in sj_vacancies['objects']
        ]

        return hh_vacancies_list + sj_vacancies_list


class Vacancy:
    """
        Базовый класс, для создания объектов  вакансий.

        Методы:
        --------
        имеет методы str и repr, и методы сравнения gt и lt
    """
    __slots__ = ['__title', '__company', '__salary', '__link']

    def __init__(self, title, company, salary, link):
        self.__title = title
        self.__company = company
        self.__salary = salary
        self.__link = link

    @property
    def title(self):
        return self.__title

    @property
    def salary(self):
        return self.__salary

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__slots__})'

    def __str__(self):
        return self.__title

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary


class HHVacancy(Vacancy):  # класс наследник, с переопределенным методом str

    def __str__(self):
        return f'HH: {self.title}, зарплата: {self.salary} руб/мес'


class SJVacancy(Vacancy):  # класс наследник, с переопределенным методом str

    def __str__(self):
        return f'SJ: {self.title}, зарплата: {self.salary} руб/мес'
