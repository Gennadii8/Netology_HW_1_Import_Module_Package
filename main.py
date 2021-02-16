from datetime import datetime

from db.people import get_employees
from application.salary import *
if __name__ == '__main__':
    get_employees()
    calculate_salary()
    current_datetime = datetime.now()
    print(current_datetime)


