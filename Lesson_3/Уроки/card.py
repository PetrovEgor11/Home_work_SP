class Card:
    number = '1234 1234 1234 1234'
    validDate = '01/99'
    holder = 'Egor'

    def __init__(self, number, date, holder):
        self.holder = holder
        self.number = number
        self.validDate = date

    def pay (self,amout):
        print("с карты", self.number, "списали", amout)