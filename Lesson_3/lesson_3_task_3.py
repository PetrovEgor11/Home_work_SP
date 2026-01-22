from Mailing import Mailing
from Adress import Address

to_addr = Address("123456", "Москва", "Ленина", "26", "750")
from_addr = Address("654321", "Санкт-Петербург", "Пушкина", "10", "5")
mailing = Mailing(to_addr, from_addr, 100, "TRACK123")
mailing.say_to_address()
