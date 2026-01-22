from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://labirint.ru")# переход на сайт
driver.maximize_window()# делает текущее окно браузера максимальным
sleep(3)
driver.minimize_window()# делает текущее окно браузера минимальным
sleep(3)
driver.fullscreen_window() # делает текущее окно браузера полноэкранным полноэкранный,
# режим обычно скрывает системные элементы, такие как панель задач и строка заголовка браузера, оставляя видимым только содержимое веб-страницы
sleep(3)

driver.set_window_size(1000,600)# делает текущее окно браузера по заданным размерам




#sleep(10)#Ожидание сек

#driver.quit()#закрыть браузер