from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

Chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

Chrome.get("https://ya.ru")
Chrome.title # Вывести название вкладки
title = Chrome.title # переменная 
print(title) # напечатать название вкладки
Chrome.quit() # Закрыть барузер

