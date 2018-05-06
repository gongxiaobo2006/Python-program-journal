#addinterest1.py
'''
def addInterest(balance,rate):
    newBalance = balance * (1+rate)
    return newBalance
'''
def addInterestList(balance,rate):
    for i in range(len(balance)):
        newBalance = balance
        newBalance[i] = balance[i] * (1+rate)
    return newBalance
'''
def main():
    amount = 1000
    rate = 0.05
    amount = addInterest(amount,rate)
    print(amount)
'''
def test():
    userBalance = [1000,500,2000,150,600]
    i = 0
    rate = 0.05
    userBalance = addInterestList(userBalance,rate)
    print(userBalance)
