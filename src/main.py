from src.connector.json_connector import JSONFileSaver
from src.api_handler.hh_handler import HeadHunterAPI
from src.api_handler.sj_handler import SuperJobAPI
from utils import get_vacancy_list
from classes import VacancyAPI

FILE_PATH = 'vacancies.json'
KEYWORD = 'Python'


def print_menu():
    print('1 - Вывести список вакансий')
    print('2 - Отсортировать по зарплате')
    print('3 - Вывести вакансию с самой большой ЗП')
    print('4 - Вывести топ три вакансии с самой высокой ЗП')
    print('5 - выход')
    print('-------------------------------------------------')

    """
    Создаем объекты для для получения данных о вакансиях
    """
def main():
    sj_api_handler = SuperJobAPI()
    hh_api_handler = HeadHunterAPI()
    json_saver = JSONFileSaver(
        file_name=FILE_PATH
    )

    """
    Чистка содержимого файла
    """
    with open(FILE_PATH, 'w') as f:
        f.truncate(0)

    vacancy_api = VacancyAPI(
        hh_api=hh_api_handler,
        sj_api=sj_api_handler
    )

    """
    Получение данных из API
    """
    vacancies_list = vacancy_api.get_vacancies(
        keyword=KEYWORD
    )

    # Сохранение данных в JSON
    json_saver.add_vacancy(
        vacancies_list
    )

    """
    Получение списка экземпляров вакансий
    """
    vac_list = get_vacancy_list(json_saver.select_vacancy())

    while True:
        print_menu()
        choice = input('Выберите действие: ')

        if choice == '1':
            for vacancy in vac_list:
                print(vacancy)
                print()
        elif choice == '2':
            sorted_vacancies = sorted(vac_list, reverse=True)
            for vacancy in sorted_vacancies:
                print(vacancy)
                print()
        elif choice == '3':
            highest_salary_vac = sorted(vac_list, reverse=True)[0]
            print(highest_salary_vac)
            print()
        elif choice == '4':
            top_three_vacancies = sorted(vac_list, reverse=True)[:3]
            for vacancy in top_three_vacancies:
                print(vacancy)
                print()
        elif choice == '5':
            break
        else:
            print('Неверный выбор. Попробуйте еще раз.')
            print()


if __name__ == '__main__':
    main()
