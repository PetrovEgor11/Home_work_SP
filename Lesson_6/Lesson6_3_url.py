from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

Chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

Chrome.get("https://ya.ru")

Chrome.current_url #Вывести URL
url = Chrome.current_url #В перменную
print(url) #Написать переменную
Chrome.quit()# Закрыть браузер