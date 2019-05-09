from datetime import datetime
from constants import CURRENCY_CODES

def validateDate(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d')
        return date <= datetime.now()
    except:
        return False

def validateCurrency(currency):
    return currency in CURRENCY_CODES

def validatePrice(price):
    try:
        return float(price) > 0
    except:
        return False