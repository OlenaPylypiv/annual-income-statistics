import unittest
from controllers import PurchaseController
from unittest.mock import MagicMock, patch
import constants.errors as errors
from models import Purchase

class TestPurchaseController(unittest.TestCase):

    @patch('controllers.models.PurchasesList')
    def setUp(self, mockedPurchasesList):
        self.testDate = '2019-05-08'
        self.testAmount = '120'
        self.testCurrency = 'UAH'
        self.testName = 'test purchase'

        mock = mockedPurchasesList.return_value
        testPurchases = [Purchase(self.testDate, self.testAmount, self.testCurrency, self.testName)]

        mock.addPurchase.return_value = testPurchases
        mock.removeByDate.return_value = []
        mock.getPurchases.return_value = testPurchases
        self.PurchaseController = PurchaseController()

    def test_report(self):

        mockCurrencyRate = 2
        self.PurchaseController.currencyService.getCurrencyRates = MagicMock(return_value={'UAH': mockCurrencyRate})

        testYear = '2019'
        testCurrency = 'EUR'
        totalSum = self.PurchaseController.report(testYear, testCurrency)

        self.assertEqual(totalSum, float(self.testAmount) / mockCurrencyRate)

    def test_addPurchase(self):


      purchases = self.PurchaseController.addPurchase(Purchase(self.testDate, self.testAmount, self.testCurrency, self.testName))

      self.assertGreater(len(purchases), 0)

    def test_removeByDate(self):
      testDate = '2019-05-12'
      self.PurchaseController.addPurchase(Purchase(self.testDate, self.testAmount, self.testCurrency, self.testName))
      purchases = self.PurchaseController.removeByDate(testDate)
      for purchase in purchases:
          self.assertNotEqual(purchase.date, testDate)


if __name__ == '__main__':
    unittest.main()