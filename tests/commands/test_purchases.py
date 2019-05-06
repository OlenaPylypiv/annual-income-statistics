import unittest
from models import Purchase
from commands import PurchaseCommands
from unittest.mock import MagicMock
import constants.errors as errors

class TestPurchaseCommands(unittest.TestCase):

    def setUp(self):
        self.testDate = '2019-05-12'
        self.testAmount = '120'
        self.testCurrency = 'UAH'
        self.testName = 'test purchase'
        self.purchaseCommands = PurchaseCommands()

    def test_report(self):

        mockCurrencyRate = 2
        self.purchaseCommands.currencyService.getCurrencyRates = MagicMock(return_value={'UAH': mockCurrencyRate})
        self.purchaseCommands.addPurchases(self.testDate, self.testAmount, self.testCurrency, self.testName)

        testYear = '2019'
        testCurrency = 'EUR'
        totalSum = self.purchaseCommands.report(testYear, testCurrency)

        self.assertEqual(totalSum, float(self.testAmount) / mockCurrencyRate)

    def test_incorrectReport(self):
        mockCurrencyRate = 2
        incorrectCurrency = 'AS'
        self.purchaseCommands.currencyService.getCurrencyRates = MagicMock(return_value={'UAH': mockCurrencyRate})

        try:
            self.purchaseCommands.addPurchases(self.testDate, self.testAmount, incorrectCurrency, self.testName)
            self.fail()
        except Exception as error:
            self.assertEqual(error.__str__(), errors.INCORRECT_CURRENCY)

    def test_addPurchase(self):


      purchases = self.purchaseCommands.addPurchases(self.testDate, self.testAmount, self.testCurrency, self.testName)

      self.assertEqual(len(purchases), 1)
      self.assertEqual(purchases[0].date, self.testDate)
      self.assertEqual(purchases[0].amount, self.testAmount)

    def test_addIncorrectPurchase(self):

        incorrectDate = '2019-15-30'
        incorrectAmount = 'asd'
        incorrectCurrency = 'AS'

        try:
          self.purchaseCommands.addPurchases(incorrectDate, self.testAmount, self.testCurrency, self.testName)
          self.fail()
        except Exception as error:
            self.assertEqual(error.__str__(), errors.INCORRECT_DATE)
        try:
          self.purchaseCommands.addPurchases(self.testDate, incorrectAmount, self.testCurrency, self.testName)
          self.fail()
        except Exception as error:
            self.assertEqual(error.__str__(), errors.INCORRECT_PRICE)
        try:
          self.purchaseCommands.addPurchases(self.testDate, self.testAmount, incorrectCurrency, self.testName)
          self.fail()
        except Exception as error:
            self.assertEqual(error.__str__(), errors.INCORRECT_CURRENCY)




    def test_removeByDate(self):
      testDate = '2019-05-12'
      self.purchaseCommands.addPurchases(self.testDate, self.testAmount, self.testCurrency, self.testName)
      purchases = self.purchaseCommands.removeByDate(testDate)
      for purchase in purchases:
          self.assertNotEqual(purchase['date'], testDate)

    def test_removeByIncorrectDate(self):
        incorrectDate = '2019-15-30'

        try:
            self.purchaseCommands.removeByDate(incorrectDate)
            self.fail()
        except Exception as error:
            self.assertEqual(error.__str__(), errors.INCORRECT_DATE)




if __name__ == '__main__':
    unittest.main()