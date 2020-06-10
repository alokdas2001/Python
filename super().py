#use of super is to access method of parent class even it is overridden 


class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")
        super().buy()

s=SmartPhone(20000, "Apple", 13)

s.buy()

'''
Inside phone constructor
Buying a smartphone
Buying a phone
'''

