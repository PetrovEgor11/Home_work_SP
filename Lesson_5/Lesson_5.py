# зайти на сайт лабиринт - есть
# Найти книги по слову Phyton
# Собрать все карточки товаров
# Вывести в консоль инфо: Название + автор + цена




from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.labirint.ru/") #Открыть сайт

serch_locator = "#search-field" #Присвоили локутору переменную

serch_input=driver.find_element(By.CSS_SELECTOR, serch_locator) #Сделали поиск латора и так же присвоили переменную для поиска локатора

serch_input.send_keys("Python") #Просим написать в локатор, а именно в строку поиска слово Python

serch_input.send_keys(Keys.RETURN) #Просим в переменной нажать кнопку Enter для выполнения поиска по странице

book_locator = "div.product-card" #Локатор для книг

books = driver.find_elements(By.CSS_SELECTOR, book_locator) #слделали поиск по лакатору и присвоили переменную

print(len(books)) #Выводим количтво по переменной 

for book in books:
    autor=book.find_element(By.CSS_SELECTOR, 'div.product-card__author').text    
    print(autor)

sleep(30)
