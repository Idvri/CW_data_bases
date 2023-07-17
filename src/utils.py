import requests


class HeadHunter:
    api = 'https://api.hh.ru/vacancies'

    def __init__(self, job_name=None):
        self.vacancies = None
        self.job_name = job_name

    def get_vacancies(self):
        response = requests.get(HeadHunter.api, params={'text': self.job_name})
        self.vacancies = response.json()['items']
        return self.vacancies
