import psycopg2


class DBManager:

    @classmethod
    def get_companies_and_vacancies_count(cls):
        """Функция получает список всех компаний и количество вакансий у каждой компании."""
        pass

    @classmethod
    def get_all_vacancies(cls):
        """Функция получает список всех вакансий с указанием названия компании, названия вакансии
         и зарплаты и ссылки на вакансию."""
        pass

    @classmethod
    def get_avg_salary(cls):
        """Функция получает среднюю зарплату по вакансиям."""
        pass

    @classmethod
    def get_vacancies_with_higher_salary(cls):
        """Функция получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        pass

    @classmethod
    def get_vacancies_with_keyword(cls):
        """Функция получает список всех вакансий, в названии которых содержатся переданные
         в метод слова, например “python”."""
        pass
