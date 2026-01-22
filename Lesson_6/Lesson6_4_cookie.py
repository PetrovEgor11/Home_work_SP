from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


my_cookie = {# переменная куки из браузера
    'name': 'cookie_policy',
    'value': '1'
}

driver.get("https://labirint.ru")# переход на сайт

driver.add_cookie(my_cookie)#добавить куки

driver.refresh()#перезагрузить страницу

driver.delete_all_cookies()#удалить все куки

#cookies = driver.get_cookie() # cookies = переменная driver.get_cookies() - получение куки от сайта
#print(cookies)
#cookie = driver.get_cookie('Имя куки') - получение информации по интересующей нас куки

driver.refresh#перезагрузить страницу

sleep(10)#Ожидание сек

driver.quit()#закрыть браузер
