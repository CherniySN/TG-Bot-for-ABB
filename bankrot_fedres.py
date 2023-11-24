from selenium import webdriver
import chromedriver_binary
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from datetime import datetime

def bankrot_fedres(inn):

    browser = webdriver.Chrome() #запускаем брайзер, может быть селениум Грид?
    browser.get('https://bankrot.fedresurs.ru/') #
    browser.implicitly_wait(2)  # что бы сайт не закрывался
    time.sleep(2)

    share = browser.find_element(By.TAG_NAME, 'el-button').click()

    try:
        find = browser.find_element(By.CSS_SELECTOR, '[formcontrolname="searchString"]')
        find.send_keys(str(inn)+"\n")
        time.sleep(1)
    except:
        print("Не найдено поле ввода!!!")

    try:
        result = browser.find_element(By.CLASS_NAME, 'no-result-msg__header')
        print(result.text)

    except:
        print("Ненайдена информация ЦСС селектором на странице!!!")
        result = "ОШИБКА"

    total_info = ['Банкротство на Федресурсе:',result.text, browser.current_url, str(datetime.now())]
    print(total_info)

    browser.close() #обяхательно закрываем сайт

    return total_info