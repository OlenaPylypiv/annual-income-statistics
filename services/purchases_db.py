import json
from typing import List, Dict
from models import Purchase

FILE_NAME = 'data.json'

class PurchaseDB:
    def transformPurchasesToJsonSerializable(self, purchases: List[Purchase]) -> List[Dict] :
        result = map(lambda x: {"date": x.date, "amount": x.amount, "currency": x.currency, "name": x.name }, purchases)
        return list(result)

    def savePurchases(self, purchases):
        jsonSerializablePurchases = self.transformPurchasesToJsonSerializable(purchases)
        with open(FILE_NAME, 'w') as f:
            json.dump(jsonSerializablePurchases, f, ensure_ascii=False)

    def transformJsonToPurchasesList(self, rawPurchases: List[Dict]) -> List[Purchase]:
        result = map(lambda x: Purchase(x["date"], x["amount"], x["currency"], x["name"]), rawPurchases)
        return list(result)

    def getPurchases(self):
        try: 
            with open('data.json') as json_file:  
                data = json.load(json_file)
                return self.transformJsonToPurchasesList(data)
        except:
            return None