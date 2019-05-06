from datetime import datetime

def validateDate(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except:
        return False

def validateCurrency(currency):
    return isinstance(currency, str) and len(currency) == 3

def validatePrice(price):
    try:
        return float(price) > 0
    except:
        return False