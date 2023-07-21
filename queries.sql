SELECT employer_name, vacancies_count FROM employers;

SELECT employer_name, vacancy_name, vacancy_salary, vacancy_url FROM vacancies
JOIN employers USING (employer_id);

SELECT AVG(vacancy_salary) FROM vacancies;

SELECT employer_name, vacancy_name, vacancy_salary, vacancy_url FROM vacancies
JOIN employers USING (employer_id)
WHERE vacancy_salary > (SELECT AVG(vacancy_salary) FROM vacancies);

SELECT employer_name, vacancy_name, vacancy_salary, vacancy_url FROM vacancies
JOIN employers USING (employer_id)
WHERE vacancy_name LIKE '%keyword%';