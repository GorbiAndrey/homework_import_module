from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

if __name__ == '__main__':
    print(datetime.strftime(datetime.now(), '%d.%m.%Y'))
    get_employees('Mike')
    calculate_salary(5)