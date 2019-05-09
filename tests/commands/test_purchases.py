import unittest
from commands import PurchaseCommands
from unittest.mock import MagicMock, patch
import constants.errors as errors
from models import Purchase

class TestPurchaseCommands(unittest.TestCase):

    @patch('commands.controllers.PurchaseController')
    def setUp(self, mockedController):
        self.testDate = '2019-05-04'
        self.testAmount = '120'
        self.testCurrency = 'UAH'
        self.testName = 'test purchase'
        
        testPurchases = [Purchase(self.testDate, self.testAmount, self.testCurrency, self.testName)]
        mock = mockedController.return_value
        mock.addPurchase.return_value = testPurchases
        mock.removeByDate.return_value = []
        self.mockReportResult = 100
        mock.report.return_value = self.mockReportResult
        self.purchaseCommands = PurchaseCommands()

    def test_report(self):

        mockCurrencyRate = 2

        testYear = '2019'
        testCurrency = 'EUR'
        totalSum = self.purchaseCommands.report(testYear, testCurrency)

        self.assertEqual(totalSum, self.mockReportResult)

    def test_incorrectReport(self):
        incorrectCurrency = 'AS'

        try:
            self.purchaseCommands.addPurchases(self.testDate, self.testAmount, incorrectCurrency, self.testName)
            self.fail()
        except Exception as error:
            self.assertEqual(error.__str__(), errors.INCORRECT_CURRENCY)

    def test_addPurchase(self):
        purchases = self.purchaseCommands.addPurchases(self.testDate, self.testAmount, self.testCurrency, self.testName)
        self.assertGreater(len(purchases), 0)
     

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
      self.purchaseCommands.addPurchases(self.testDate, self.testAmount, self.testCurrency, self.testName)
      purchases = self.purchaseCommands.removeByDate(self.testDate)
      for purchase in purchases:
          self.assertNotEqual(purchase.date, self.testDate)

    def test_removeByIncorrectDate(self):
        incorrectDate = '2019-15-30'

        try:
            self.purchaseCommands.removeByDate(incorrectDate)
            self.fail()
        except Exception as error:
            self.assertEqual(error.__str__(), errors.INCORRECT_DATE)




if __name__ == '__main__':
    unittest.main()