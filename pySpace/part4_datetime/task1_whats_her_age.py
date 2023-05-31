from datetime import datetime, date,timedelta

def get_age(birth_date, current_date=None):
    today = date.today() if current_date == None else current_date
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))