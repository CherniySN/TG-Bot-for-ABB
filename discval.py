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
    browser.get('https://service.nalog.ru/disqualified.do')
    browser.implicitly_wait(2)  # что бы сайт не закрывался
    time.sleep(1)

    try:
        input_innPRS = browser.find_element(By.ID, 'query')
        send_keys_with_delays(input_innPRS, str(inn), browser)

    except:
        print("Ненайдено поле ввода")

    try:
        browser.find_element(By.ID, 'btnSearch').click()
        time.sleep(1)
    except:
        print("Ненайдена кнопка")

    try:
        res = browser.find_element(By.ID, 'pnlResult').text
    except:
        result = "ОШИБКА"
        print("Ненайдена кнопка")

    total_info = ['РЕЕСТР ДИСКВАЛИФИЦИРОВАННЫХ ЛИЦ', res, browser.current_url, str(datetime.now())]
    print(total_info)
    browser.close() #обяхательно закрываем сайт

    return total_info

