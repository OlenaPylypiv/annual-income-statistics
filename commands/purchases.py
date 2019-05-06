import itertools
from datetime import datetime
from typing import List
from models import Purchase
from services import CurrencyService
from validators import validateCurrency, validateDate, validatePrice
import constants.errors as errors

class PurchaseCommands:

    def __init__(self):
        self.__purchases: List[Purchase] = []
        self.currencyService = CurrencyService()

    def showAll(self):
        sortedPurchases = self.__purchases
        sortedPurchases.sort(key=lambda x: datetime.strptime(x.date, '%Y-%m-%d'))

        purchases_groups = itertools.groupby(sortedPurchases, lambda x: x.date)
        groupedPurchases = [{'date': date, 'values': [x for x in values]} for date, values in purchases_groups]

        resultString = ''
        for el in groupedPurchases:
            resultString += el['date'] + '\n'
            for value in el['values']:
                resultString +='{} {} {} \n'.format(value.name, value.amount, value.currency)
            resultString += '\n'

        print(resultString)

    def addPurchases(self, date, amount, currency, name):
        if not validateDate(date):
            raise Exception(errors.INCORRECT_DATE)
        if not validatePrice(amount):
            raise Exception(errors.INCORRECT_PRICE)
        if not validateCurrency(currency):
            raise Exception(errors.INCORRECT_CURRENCY)

        self.__purchases.append(Purchase(date, amount, currency, name))
        self.showAll()

        return self.__purchases


    def removeByDate(self, date):
        if not validateDate(date):
            raise Exception(errors.INCORRECT_DATE)

        for i, val in enumerate(self.__purchases):
            if val.date == date:
                self.__purchases.pop(i)
        self.showAll()

        return self.__purchases


    def getCurrencyList(self):
        avaliableCurrancies = []
        for i, val in enumerate(self.__purchases):
            if val.currency not in avaliableCurrancies:
                avaliableCurrancies.append(val.currency)
        return avaliableCurrancies


    def report(self, year, baseCurrency):
        if not validateCurrency(baseCurrency):
            raise Exception(errors.INCORRECT_CURRENCY)

        rates = self.currencyService.getCurrencyRates(baseCurrency, self.getCurrencyList())
        totalSum = 0
        for i, val in enumerate(self.__purchases):
            date, *_ = val.date.split('-')
            if date == year:
                totalSum += float(val.amount)/rates[val.currency]

        if (totalSum != 0):
            print(str(totalSum) + ' EUR')
        else:
            print('There are no record on {} year '.format(year))
        return totalSum
