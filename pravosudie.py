from selenium import webdriver
import chromedriver_binary
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from datetime import datetime

def pravosud(inn):
    browser = webdriver.Chrome() #запускаем брайзер, может быть селениум Грид?
    browser.get('https://bsr.sudrf.ru/bigs/portal.html')
    browser.implicitly_wait(5)  # что бы сайт не закрывался
    time.sleep(5)

    try:
        find = browser.find_element(By.CSS_SELECTOR, '[id="portalSearchInput"]')
        find.send_keys(inn)
        time.sleep(1)
    except:
        print("Не найдено поле ввода")

    try:
        browser.find_element(By.CLASS_NAME, 'buttonOuter').click()
    except:
        print("Кнопка не найдена")

    try:
        result = browser.find_element(By.CLASS_NAME, 'noBreakText')
        result = result.text

    except:
        print("Ненайдена информация ЦСС селектором на странице")
        result = "Ошибка"

    total_info = ['Поиск по делам и судебным актам по 262-ФЗ:', result, browser.current_url, str(datetime.now())]
    print(total_info)
    browser.close() #обяхательно закрываем сайт
    return total_info