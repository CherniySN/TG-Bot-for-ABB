from selenium import webdriver
import chromedriver_binary
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from datetime import datetime

def kompromat(inn):
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    browser = webdriver.Chrome() #запускаем брайзер, может быть селениум Грид?
    browser.get('https://search.compromat.ru/')
    browser.implicitly_wait(2)  # что бы сайт не закрывался
    time.sleep(1)

    try:
        find = browser.find_element(By.NAME, 'q')
        find.send_keys(inn+"\n")
        time.sleep(1)
    except:
        print("Не найдено поле ввода, необходимо обратиться в службу технической поддержки.")

    try:
        res = browser.find_element(By.TAG_NAME, 'small').text

    except:
        print("Ненайдена информация ЦСС селектором на странице, необходимо обратиться в службу технической поддержки.")
        result = "ОШИБКА"

    total_info = ['ПОИСК СТАТЕЙ НА КМПРОМАТ.РУ ', res, browser.current_url, str(datetime.now())]
    browser.close() #обяхательно закрываем сайт
    return total_info

#print(kompromat("Ак Барс банк\n"))