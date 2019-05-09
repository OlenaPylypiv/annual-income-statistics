from datetime import datetime
from constants import CURRENCY_CODES

def validateDate(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except:
        return False

def validateCurrency(currency):
    return currency in CURRENCY_CODES

def validatePrice(price):
    try:
        return float(price) > 0
    except:
        return False