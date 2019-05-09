from models import Purchase
import controllers
from validators import validateCurrency, validateDate, validatePrice
import constants.errors as errors

class PurchaseCommands:

    def __init__(self):
        self.controller = controllers.PurchaseController()

    def showAll(self):
       return self.controller.showAll()

    def addPurchases(self, date, amount, currency, name):
        if not validateDate(date):
            raise Exception(errors.INCORRECT_DATE)
        if not validatePrice(amount):
            raise Exception(errors.INCORRECT_PRICE)
        if not validateCurrency(currency):
            raise Exception(errors.INCORRECT_CURRENCY)

        return self.controller.addPurchase(Purchase(date, amount, currency, name))


    def removeByDate(self, date):
        if not validateDate(date):
            raise Exception(errors.INCORRECT_DATE)

        return self.controller.removeByDate(date)


    def report(self, year, baseCurrency):
        if not validateCurrency(baseCurrency):
            raise Exception(errors.INCORRECT_CURRENCY)

        return self.controller.report(year, baseCurrency)
