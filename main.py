# Импортируем основной модуль Selenium WebDriver для автоматизации браузера
from selenium import webdriver
# Импортируем Service из модуля chrome.webdriver, чтобы использовать сервис драйвера Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
# Импортируем ChromeDriverManager из библиотеки webdriver-manager для автоматической установки драйвера
from webdriver_manager.chrome import ChromeDriverManager

# Создаем объект опций браузера Chrome, чтобы настроить его поведение
options = webdriver.ChromeOptions()
# Добавляем экспериментальную опцию, которая предотвращает закрытие браузера после выполнения скрипта
options.add_experimental_option("detach", True)
# Создаем экземпляр веб-драйвера Chrome:
# - Используем ChromeDriverManager().install() для автоматической загрузки драйвера
# - Передаем options, чтобы браузер не закрывался после выполнения
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
# Задаем базовый URL сайта, на который будем заходить
base_url = 'http://www.saucedemo.com/'
# Открываем указанный сайт в браузере
driver.get(base_url)
# Устанавливаем размер окна браузера (ширина 1920 пикселей, высота 1080 пикселей)
driver.set_window_size(1920, 1080)