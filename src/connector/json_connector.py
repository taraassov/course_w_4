import json

from src.connector.abstract_connector import JSONSaver


class JSONFileSaver(JSONSaver):
    """
        Класс, который сохраняет и извлекает данные о вакансиях в формате JSON из файла.

        Методы:
        --------
        add_vacancy
            Добавляет вакансию в файл JSON.

        select_vacancy
            Извлекает все вакансии из файла JSON.

        delete_vacancy
            Удаляет вакансию из файла JSON.
    """
    def __init__(self, file_name):
        self.file_name = file_name


    def add_vacancy(self, vacancy):
        with open(self.file_name, 'a', encoding='utf-8') as file:
            json.dump(vacancy, file, ensure_ascii=False, indent=4)


    def select_vacancy(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            return json.load(file)


    def delete_vacancy(self, vacancy):
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
        with open(self.file_name, 'w') as file:
            for line in lines:
                if json.loads(line) != vacancy.__dict__:
                    file.write(line)
