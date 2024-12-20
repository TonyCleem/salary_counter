from terminaltables import DoubleTable


def create_table_rub_salary(salaries, title):
    table_header = [
    ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата']
    ]

    for salary in salaries:
        table_header.append(salary)


    table_rub_salary = DoubleTable(table_header, title)


    return table_rub_salary
