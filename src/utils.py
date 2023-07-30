from classes import HHVacancy, SJVacancy


def get_salary_from_hh_vacancy(salary_dict):
    """
        Получает зарплату из словаря вакансий HeadHunter.

        Возвращает:
        Возвращает 0, если словарь равен None.
    """
    if salary_dict is not None:

        if salary_dict['from'] is not None:
            return salary_dict['from']
        else:
            return salary_dict['to']

    return 0


def get_vacancy_list(jsreader):
    """
        Преобразует объект JSON в список объектов Vacancy.

        Возвращает:
            Список объектов вакансии.
    """
    vacancies_list = []

    for item in jsreader:

        if item['source'] == 'hh':

            vacancies_list.append(
                HHVacancy(
                    title=item['title'],
                    company=item['company'],
                    salary=get_salary_from_hh_vacancy(item['salary']),
                    link=item['link']
                ))

        elif item['source'] == 'sj':

            vacancies_list.append(
                SJVacancy(
                    title=item['title'],
                    company=item['company'],
                    salary=item['salary'] if item['salary'] is not None else 0,
                    link=item['link']
                ))
    return vacancies_list
