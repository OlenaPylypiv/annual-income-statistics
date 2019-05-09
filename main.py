import shlex
from commands import PurchaseCommands
import constants.purchase_commands as commandNames

purchaseCommands = PurchaseCommands()


while(1):
    try:
        userInput = input(' ')
        command, *params = shlex.split(userInput)

        if (command == commandNames.EXIT) :
            break
        if (command == commandNames.PURCHASE):
            purchaseCommands.addPurchases(*params)
        if (command == commandNames.ALL):
            purchaseCommands.showAll()
        if (command == commandNames.CLEAR):
            purchaseCommands.removeByDate(*params)
        if (command == commandNames.REPORT):
            purchaseCommands.report(*params)
    except Exception as error:
        print('Program failed. Error: {}'.format(error.__str__()))
        raise error





