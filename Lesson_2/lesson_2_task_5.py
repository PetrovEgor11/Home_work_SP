def month_to_season(mouth):
    if mouth in (1,2,12):
        print("Зима")
    elif mouth in (3,4,5):
        print("Весна")
    elif mouth in (6,7,8):
        print("Лето")
    elif mouth in (9,10,11):
        print("Осень")
    else:
        print("Некорректный номер месяца")
mouth=int(input("Введите номер месяца:"))
month_to_season(mouth)