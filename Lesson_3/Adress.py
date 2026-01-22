class Address:
    def __init__(self, index, city, street, house, apartment):
<<<<<<< HEAD
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def __str__(self):
        return f"{self.index}, {self.city}, {self.street}, {self.house}, {self.apartment}."
=======
        self.index=index
        self.city=city
        self.street=street
        self.house=house
        self.apartament=apartment


    def say_index (self):
        print ("Индекс:", self.index)

    def say_city (self):
        print ("Город:", self.city)

    def say_sreeet (self):
        print ("Улица:", self.street)

    def say_house (self):
        print ("Дом:", self.house)
    
    def say_aapartament (self):
        print ("Номер квартиры:", self.apartament)

from_adrr = Address ()
from_adrr.say_index()
from_adrr.say_city()
from_adrr.say_sreeet()
from_adrr.say_house()
from_adrr.say_aapartament()
>>>>>>> 46d3bce43b51188378bb94e45a710a75787c8dde
