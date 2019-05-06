import requests
import constants.errors as errors

CURRENCY_ENDPOINT = 'http://data.fixer.io/api/latest'
API_KEY = 'e35361a61a0e88224e2c8eb53bda1a88'

class CurrencyService:
    def getCurrencyRates(self, baseCurrency, currenciesList):
        url = '{}?access_key={}&base={}&symbols={}'.format(CURRENCY_ENDPOINT, API_KEY, baseCurrency, ','.join(currenciesList))
        try:
            response = requests.get(url)
            jsonRes = response.json()
            if jsonRes['success']:
                if 'rates' in jsonRes:
                    return jsonRes['rates']
                else:
                    raise Exception(errors.MISSING_RATES)
            else:
                raise Exception(errors.UNSUCCESSFUL_CURRENCY_SERVICE_RESPONSE.format(jsonRes['error']['type']))
        except Exception as error:
            raise error