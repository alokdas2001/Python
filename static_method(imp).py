class phone:
    discount = 50

    @staticmethod
    def price(cost):
        print(cost-phone.discount)  # you have to call class_name.variable (phone.discount)

print(phone.price(10000))  # without creating object calling methods
