from selenium import webdriver
import chromedriver_binary
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait

def send_keys_with_delays(element, value, browser):
    wait = WebDriverWait(browser, 10)
    for i in range(len(value)):
        element.send_keys(value[i])
        wait.until(lambda _: element.get_property('value')[:i] == value[:i])

def obreldoc(inn):
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    browser = webdriver.Chrome() #запускаем брайзер, может быть селениум Грид?
    browser.get('https://service.nalog.ru/bi.do')
    browser.implicitly_wait(2)  # что бы сайт не закрывался
    time.sleep(1)

    try:
        browser.find_element(By.ID, 'unirad_0').click()
        time.sleep(1)
    except:
        print("Не найден чек-бокс")

    try:
        input_innPRS = browser.find_element(By.ID, 'innPRS')#.send_keys(inn)
        send_keys_with_delays(input_innPRS, str(inn), browser)
        input_bikPRS = browser.find_element(By.ID, 'bikPRS')#.send_keys(1653001805)
        send_keys_with_delays(input_bikPRS, str(1653001805), browser)
    except:
        print("Ненайдено поле ввода")

    try:
        browser.find_element(By.ID, 'btnSearch').click()
        time.sleep(1)
    except:
        print("Ненайдена кнопка")

    try:
        res = browser.find_element(By.ID, 'pnlResultData').text
    except:
        result = "ОШИБКА"
        print("Ненайдена кнопка")

    total_info = ['СИСТЕМА ИНФОРМИРОВАНИЯ БАНКОВ О СОСТОЯНИИ ОБРАБОТКИ ЭЛЕКТРОННЫХ ДОКУМЕНТОВ', res, browser.current_url, str(datetime.now())]
    browser.close() #обяхательно закрываем сайт
    return total_info
