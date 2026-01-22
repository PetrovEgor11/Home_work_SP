# def fizz_buzz (n):
#     if n % 3:
#         print ("Fizz")
#     elif n % 5:
#         print ("Buzz")
#     if n % 3 and n % 5:
#         print ("FizzBuzz")

# n = int(input("Введите число:"))
# result = fizz_buzz
# print (result)



def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

n = int(input("Введите число: "))
fizz_buzz(n)
