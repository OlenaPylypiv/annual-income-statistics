from typing import List
from models import Purchase

def printGroupedPurchases(groupedPurchases):
    resultString = ''
    for el in groupedPurchases:
        resultString += el['date'] + '\n'
        for value in el['values']:
            resultString +='{} {} {} \n'.format(value.name, value.amount, value.currency)
        resultString += '\n'
    print(resultString)

def printPurchasesReport(totalSum, baseCurrency, year):
    if (totalSum != 0):
        print("{} {}".format(str(totalSum), baseCurrency))
    else:
        print('There are no record on {} year '.format(year))
    