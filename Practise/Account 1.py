class Account:

    def __init__(self, owner, currency = "CAD", balance = 0):

        self.currLst = {
            "USD" : [1.34607, "$"],
            "EUR" : [1.51746, "€"],
            "GBP" : [1.70233, "£"],
            "CNY" : [0.0189917, "¥"],
            "INR" : [0.0178035, "₹"],
            "CAD" : [1, "$"]
        }
        self.__owner = owner

        #if currency not in self.currLst:
           # raise ValueError("ERROR: Unsupported currency type")
        self.__balance = balance
        self._currency = currency #this calls the currency setter attribute
        

    def deposit(self, amt):
        if amt < 0:
            raise ValueError("ERROR: Value for "\
                             "deposit/withdraw is restricted to positive values")
        self.__balance += amt

    def withdraw(self, amt):
        if amt < 0:
            raise ValueError("ERROR: Value for "\
                             "deposit/withdraw is restricted to positive values")
        self.__balance -= amt

    def __str__(self):
        return "Owner: " + self.__owner + "\nBalance: " + self.currLst[self.currency][1] + \
              str(self.__balance)
    
    def __eq__(self, other):
        a2_balance = round(other.__balance * other.currLst[other.currency][0], 2)
        return self.__balance == a2_balance
    
    def __add__(self, other):
        a2_balance = round(other.__balance * other.currLst[other.currency][0], 2)
        return Account(self.__owner, self.currency, self.__balance + a2_balance)
    
    @property
    def currency(self):
        c=  self._currency
        return c
    
    @currency.setter
    def currency(self, cr):
        if cr not in self.currLst:
            raise ValueError("ERROR: Unsupported currency type")
        self.__balance = round(self.__balance *  self.currLst[ self._currency][0], 2)
        self._currency = cr #calling propert

#main
a1 = Account("Aaron") #CAD, 0
a2 = Account("Jim", "USD", 1000) #USD, 1000
print(a1 == a2)
print(a1 + a2)
a2.currency = "CAD"
a3 = Account("Ryan", balance = 1000) #CAD, 1000