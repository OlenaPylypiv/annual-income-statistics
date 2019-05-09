from copy import deepcopy
from typing import List
from models import Purchase
from services import PurchaseDB

class PurchasesList:
    def __init__(self):
        self.purchaseDB = PurchaseDB()
        self.__purchases: List[Purchase] = self.purchaseDB.getPurchases() or []

    def addPurchase(self, purchase: Purchase):
        self.__purchases.append(purchase)
        self.purchaseDB.savePurchases(self.__purchases)

    def removeByDate(self, date):
        self.__purchases = [purchase for purchase in self.__purchases if purchase.date != date]
        self.purchaseDB.savePurchases(self.__purchases)
    
    def getPurchases(self):
        return deepcopy(self.__purchases)