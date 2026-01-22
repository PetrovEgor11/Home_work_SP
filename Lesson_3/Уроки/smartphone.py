class Smartphone:
    def __init__(self, marka, model_tel, number_tel):
        self.marka = marka
        self.model_tel = model_tel
        self.number_tel = number_tel

    def __str__(self):
        return f"Марка: {self.marka}, Модель: {self.model_tel}, Номер: {self.number_tel}"
#     def sayMarka (self):
#         print("Марка моего телефона:", self.marka)

#     def sayModel_tel (self):
#         print ("Модель моего телефона:", self.model_tel)

#     def sayNumber_tel (self):
#         print ("Номер моего телефона:", self.number_tel)

# user = Smartphone ("Iphone", "12", "89154908269")
# user.sayMarka()
# user.sayModel_tel()
# user.sayNumber_tel()
