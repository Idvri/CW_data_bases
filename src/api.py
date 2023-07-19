import requests


class HeadHunter:
    api = 'https://api.hh.ru/vacancies'

    def __init__(self, job_name=None):
        self.vacancies = None
        self.job_name = job_name

    def get_vacancies(self):
        response = requests.get(HeadHunter.api, params={'text': self.job_name, 'employer_id': {'1740', '78638',
                                                                                               '3009025', '1868342',
                                                                                               '652744', '9739229',
                                                                                               '5714322', '9632510',
                                                                                               '83554694', '9288781'}})
        self.vacancies = response.json()['items']
        return self.vacancies
