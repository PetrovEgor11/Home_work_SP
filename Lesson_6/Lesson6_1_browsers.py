from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

#browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

#browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def make_screenshoot(browser):
    browser.maximize_window() #Увеичиваем размер окна бразузера до максимального
    browser.get("https://ya.ru") #Открывает сайт 
    sleep(5) #Ожидаем 5 секунд
    
    browser.save_screenshot('./ya_'+browser.name+' .png') #Сделать скрин 
    browser.quit()#Закрыть браузер

Chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
Firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

make_screenshoot(Chrome)
make_screenshoot(Firefox)

