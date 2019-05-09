import unittest
from unittest.mock import Mock, patch
from services import CurrencyService
import constants.errors as errors

class TestCurrencyService(unittest.TestCase):
    @patch('services.requests.get')
    def test_getCurrencyRates(self, mockGet):
        mockedResponse = {
            "success":True,
            "timestamp":1557168845,
            "base":"EUR",
            "date":"2019-05-06",
            "rates": {
                "UAH":4,
                "PLN":6,
                "EUR": 2
            }
        }
        mockGet.return_value = Mock(ok=True)
        mockGet.return_value.json.return_value = mockedResponse

        testBaseCurrency = "EUR"
        testCurrenciesList = ["UAH", "PLN"]
        currencyService = CurrencyService()

        rates = currencyService.getCurrencyRates(testBaseCurrency, testCurrenciesList)
        self.assertEqual(rates,{"UAH":2,"PLN":3,"EUR":1})

    @patch('services.requests.get')
    def test_getCurrencyRatesWithEmptyResponse(self, mockGet):
        mockedResponse = {
            "success": True,
            "timestamp": 1557168845,
            "base": "EUR",
            "date": "2019-05-06"
        }
        mockGet.return_value = Mock(ok=True)
        mockGet.return_value.json.return_value = mockedResponse

        testBaseCurrency = "EUR"
        testCurrenciesList = ["UAH", "PLN"]
        currencyService = CurrencyService()

        try:
            currencyService.getCurrencyRates(testBaseCurrency, testCurrenciesList)
            self.fail()
        except Exception as error:
            self.assertEqual(error.__str__(), errors.MISSING_RATES)