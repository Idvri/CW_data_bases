from src.api import HeadHunter
from src.cls import DBManager
from psycopg2.errors import UniqueViolation

if __name__ == "__main__":

    print('''Добрый день! Эта утилита предназначена для работы с вакансиями, хранящимися в базе данных.
Выберите, указав цифру, что хотите сделать или напишите "выйти", чтобы закончить сеанс.\n
1. Получить список всех компаний и количество вакансий у каждой компании;
2. Получить список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию;
3. Получить среднюю зарплату по вакансиям;
4. Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям;
5. Получить список всех вакансий, в названии которых содержатся переданные в метод слова, например "python".

Загрузка...''')

    companies = HeadHunter.employers

    for company in companies:
        try:
            DBManager.get_emp_data_saved(HeadHunter.get_employer_info(company))
        except UniqueViolation:
            continue
        finally:
            vacancies = HeadHunter.get_vacancies(company)
            for vacancy in vacancies:
                try:
                    DBManager.get_vac_data_saved(vacancy)
                except UniqueViolation:
                    continue

    while True:
        user_choice = input('\nВаш выбор: ').lower()

        if user_choice == 'выйти':

            print('\nВы вышли из программы. Сеанс завершен.')
            break

        elif int(user_choice) == 1:

            print('\nВыгружаем информацию по вашему запросу...\n')
            for info in DBManager.get_companies_and_vacancies_count():
                print(f'Название компании: {info[0]}. Кол-во вакансий: {info[1]}.')
            print('\nЧто-то ещё?')

        elif int(user_choice) == 2:

            print('\nВыгружаем информацию по вашему запросу...')
            for info in DBManager.get_all_vacancies():
                print(f'''\nНазвание компании: {info[0]}. 
Название вакансии: {info[1]}.
Размер зарплаты: {info[2]} руб.
Ссылка на вакансию: {info[3]}.''')
            print('\nЧто-то ещё?')

        elif int(user_choice) == 3:

            print('\nВыгружаем информацию по вашему запросу...\n')
            print(f'Средняя зарплата по вакансиям: {DBManager.get_avg_salary()} руб.')
            print('\nЧто-то ещё?')

        elif int(user_choice) == 4:

            print('\nВыгружаем информацию по вашему запросу...')
            for info in DBManager.get_vacancies_with_higher_salary():
                print(f'''\nНазвание компании: {info[0]}. 
Название вакансии: {info[1]}.
Размер зарплаты: {info[2]} руб.
Ссылка на вакансию: {info[3]}.''')
            print('\nЧто-то ещё?')

        elif int(user_choice) == 5:
            keyword = input('\nВведите ключевое слово: ')
            print('\nВыгружаем информацию по вашему запросу...')
            vacancies_with_keyword = DBManager.get_vacancies_with_keyword(keyword)

            if len(vacancies_with_keyword) == 0:
                print('\nТаких вакансий нет.')
            else:
                for info in vacancies_with_keyword:
                    print(f'''\nНазвание компании: {info[0]}. 
Название вакансии: {info[1]}.
Размер зарплаты: {info[2]} руб.
Ссылка на вакансию: {info[3]}.''')

            print('\nЧто-то ещё?')

        else:
            print('\nВы указали не существующий вариант выбора. Попробуйте ещё раз!')
