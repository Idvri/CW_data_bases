import csv

import psycopg2
from src.api import HeadHunter


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

    @classmethod
    def get_emp_data_saved(cls, employer):
        with psycopg2.connect(host='localhost', database='CW_DB', user='postgres', password='Nodar126') as connection:
            with connection.cursor() as cur:

                info = (employer['id'], employer['name'], employer['open_vacancies'])
                cur.execute('INSERT INTO employers VALUES (%s, %s, %s)', tuple(info))

    @classmethod
    def get_vac_data_saved(cls, vacancy):
        with psycopg2.connect(host='localhost', database='CW_DB', user='postgres', password='Nodar126') as connection:
            with connection.cursor() as cur:

                if vacancy['salary']['to'] == 'None':
                    if vacancy['salary']['currency'] != 'RUR':
                        vac_salary = str(int(vacancy['salary']['from']) * 90)
                elif vacancy['salary']['currency'] != 'RUR':
                    vac_salary = str(int(vacancy['salary']['to']) * 90)
                else:
                    vac_salary = str(vacancy['salary']['to'])

                info = (vacancy['id'], vacancy['employer']['id'], vacancy['name'], vac_salary, vacancy['alternate_url'])
                cur.execute('INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s)', tuple(info))
