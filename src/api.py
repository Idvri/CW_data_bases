import requests


class HeadHunter:
    api = 'https://api.hh.ru/vacancies'
    employers = ('1740', '78638',
                 '3009025', '1868342',
                 '652744', '9739229',
                 '5714322', '9632510',
                 '83554694', '9288781')

    @classmethod
    def get_vacancies(cls, employer):
        response = requests.get(HeadHunter.api, params={'employer_id': employer})
        vacancies = response.json()['items']
        return vacancies
