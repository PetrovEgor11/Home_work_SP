class Mailing:

    def __init__(self, to_address, from_address, cost, track):
<<<<<<< HEAD
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track
    
    def __str__(self):
        return f"Отправление {self.track} из {self.to_address} в {self.from_address}. Стоимость: {self.cost} рублей."
=======
        self.to_address=to_address
        self.from_address=from_address
        self.cost=cost
        self.track=track
        
    def say_to_address (self):
        print ("Обращаться к", self.to_address)

    def say_from_address (self):
        print ("С адреса", self.from_address)

    def say_cost (self):
        print ("Стоимость", self.cost)

    def say_track (self):
        print ("Дом", self.track)

Mail=Mailing ()
Mail.say_to_address()
Mail.say_from_address()
Mail.say_cost()
Mail.say_track()
>>>>>>> 46d3bce43b51188378bb94e45a710a75787c8dde
