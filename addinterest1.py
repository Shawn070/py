'''
函数的形参只接收了实参的值，给形赋值并不影响实参。
可以通过值来传递参数。
'''
def addInterest(balance, rate):
    newBalance = balance * (1 + rate)
    # balance = newBalance
    return newBalance
def main():
    amount = 1000
    rate = 0.05
    # addInterest(amount, rate)
    amount = addInterest(amount, rate)
    print(amount)
main()