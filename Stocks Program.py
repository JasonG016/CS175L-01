#Jason Galvao
#CS175L-02
#stocks

commissionRate = float(input('enter the commission rate'))
numShares = int(input('enter number of shares'))
purchasePrice = float(input('enter purchase price'))
sellingPrice = float(input('enter selling price'))

amountPaidForStock = numShares * purchasePrice
purchaseCommission = commissionRate * amountPaidForStock
totalPaid= amountPaidForStock + purchaseCommission
stockSoldFor= numShares + sellingPrice
sellingCommission = commissionRate + stockSoldFor
totalReceived= stockSoldFor - sellingCommission
profitOrLoss = totalReceived - sellingCommission

print('Amout paid for stock:$',amountPaidForStock)
print('Comission piad for purchase:$',purchaseCommission)
print('Amout the stock sold for:$',stockSoldFor)
print('Commission paid for on the sale:',sellingCommission)
print('Profit or loss:',profitOrLoss)
