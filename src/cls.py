import psycopg2
from decimal import Decimal


class DBManager:

    @classmethod
    def get_companies_and_vacancies_count(cls):
        """Функция получает список всех компаний и количество вакансий у каждой компании."""
        with psycopg2.connect(host='localhost', database='CW_DB', user='postgres', password='Nodar126') as connection:
            with connection.cursor() as cur:
                cur.execute('SELECT employer_name, vacancies_count FROM employers')
                companies_and_vacancies = cur.fetchall()
                return companies_and_vacancies

    @classmethod
    def get_all_vacancies(cls):
        """Функция получает список всех вакансий с указанием названия компании, названия вакансии
         и зарплаты и ссылки на вакансию."""
        with psycopg2.connect(host='localhost', database='CW_DB', user='postgres', password='Nodar126') as connection:
            with connection.cursor() as cur:
                cur.execute('SELECT employer_name, vacancy_name, vacancy_salary, vacancy_url FROM vacancies '
                            'JOIN employers USING (employer_id)')
                all_vacancies = cur.fetchall()
                return all_vacancies

    @classmethod
    def get_avg_salary(cls):
        """Функция получает среднюю зарплату по вакансиям."""
        with psycopg2.connect(host='localhost', database='CW_DB', user='postgres', password='Nodar126') as connection:
            with connection.cursor() as cur:
                cur.execute('SELECT AVG(vacancy_salary) FROM vacancies')
                avg_salary = cur.fetchall()[0][0]
                avg_salary = Decimal(avg_salary)
                return avg_salary.quantize(Decimal("1.00"))

    @classmethod
    def get_vacancies_with_higher_salary(cls):
        """Функция получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        with psycopg2.connect(host='localhost', database='CW_DB', user='postgres', password='Nodar126') as connection:
            with connection.cursor() as cur:
                cur.execute('SELECT employer_name, vacancy_name, vacancy_salary, vacancy_url FROM vacancies '
                            'JOIN employers USING (employer_id)'
                            'WHERE vacancy_salary > (SELECT AVG(vacancy_salary) FROM vacancies)')
                high_sal_vac = cur.fetchall()
                return high_sal_vac

    @classmethod
    def get_vacancies_with_keyword(cls, keyword):
        """Функция получает список всех вакансий, в названии которых содержатся переданные
         в метод слова, например 'python'."""
        with psycopg2.connect(host='localhost', database='CW_DB', user='postgres', password='Nodar126') as connection:
            with connection.cursor() as cur:
                cur.execute("SELECT employer_name, vacancy_name, vacancy_salary, vacancy_url FROM vacancies "
                            "JOIN employers USING (employer_id) "
                            f"WHERE vacancy_name LIKE '%{keyword}%'")
                vacancies_with_keyword = cur.fetchall()
                return vacancies_with_keyword

    @classmethod
    def get_emp_data_saved(cls, employer):
        with psycopg2.connect(host='localhost', database='CW_DB', user='postgres', password='Nodar126') as connection:
            with connection.cursor() as cur:
                info = (employer['id'], employer['name'], employer['open_vacancies'])
                cur.execute('INSERT INTO employers VALUES (%s, %s, %s)', tuple(info))
                connection.close()

    @classmethod
    def get_vac_data_saved(cls, vacancy):
        with psycopg2.connect(host='localhost', database='CW_DB', user='postgres', password='Nodar126') as connection:
            with connection.cursor() as cur:
                if vacancy['salary']['to'] is None:

                    if vacancy['salary']['currency'] != 'RUR':
                        vac_salary = str(int(vacancy['salary']['from']) * 90)
                    else:
                        vac_salary = str(vacancy['salary']['from'])

                elif vacancy['salary']['currency'] != 'RUR':
                    vac_salary = str(int(vacancy['salary']['to']) * 90)

                else:
                    vac_salary = str(vacancy['salary']['to'])

                info = (vacancy['id'], vacancy['employer']['id'], vacancy['name'], vac_salary, vacancy['alternate_url'])
                cur.execute('INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s)', tuple(info))
