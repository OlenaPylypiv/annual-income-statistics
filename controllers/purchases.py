import itertools
from datetime import datetime
import models
from services import CurrencyService
from utils import printGroupedPurchases, printPurchasesReport

class PurchaseController:
    def __init__(self):
        self.currencyService = CurrencyService()
        self.purchases = models.PurchasesList()

    def addPurchase(self, purchase: models.Purchase):
        self.purchases.addPurchase(purchase)
        self.showAll()

        return self.purchases.getPurchases()

    def showAll(self):
        sortedPurchases = self.purchases.getPurchases()
        sortedPurchases.sort(key=lambda x: datetime.strptime(x.date, '%Y-%m-%d'))

        purchases_groups = itertools.groupby(sortedPurchases, lambda x: x.date)
        groupedPurchases = [{'date': date, 'values': [x for x in values]} for date, values in purchases_groups]

        printGroupedPurchases(groupedPurchases)

    def removeByDate(self, date):
        self.purchases.removeByDate(date)
        self.showAll()

        return self.purchases.getPurchases()

    def getCurrencyList(self):
        avaliableCurrancies = []
        for val in self.purchases.getPurchases():
            if val.currency not in avaliableCurrancies:
                avaliableCurrancies.append(val.currency)
        return avaliableCurrancies
    
    def report(self, year, baseCurrency):

        rates = self.currencyService.getCurrencyRates(baseCurrency, self.getCurrencyList())
        totalSum = 0
        for val in self.purchases.getPurchases():
            date, *_ = val.date.split('-')
            if date == year:
                totalSum += float(val.amount)/rates[val.currency]

        printPurchasesReport(totalSum, baseCurrency, year)
        return totalSum
