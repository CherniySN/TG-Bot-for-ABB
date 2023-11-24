from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_binary
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from datetime import datetime

def send_keys_with_delays(element, value, browser):
    wait = WebDriverWait(browser, 10)
    for i in range(len(value)):
        element.send_keys(value[i])
        wait.until(lambda _: element.get_property('value')[:i] == value[:i])

def fns_rossii_inn(fam, nam, otch, bdate, docno, docdt):
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')

    browser = webdriver.Chrome()  # запускаем брайзер, может быть селениум Грид?
    browser.get('https://service.nalog.ru/static/personal-data.html?svc=inn&from=%2Finn.html')
    browser.implicitly_wait(2)  # что бы сайт не закрывался
    time.sleep(1)

    try:
        browser.find_element(By.ID, 'unichk_0').click()
    except:
        print("Не найден чек бокс")

    try:
        finde = browser.find_element(By.ID, 'btnContinue').click()
        time.sleep(2)
    except:
        print("Кнопка не найдена")

    try:
        input_form_fam = browser.find_element(By.CSS_SELECTOR, '[id="fam"]')
        send_keys_with_delays(input_form_fam, fam,browser)
        input_form_nam = browser.find_element(By.ID, 'nam')
        send_keys_with_delays(input_form_nam, nam,browser)
        input_form_otch = browser.find_element(By.ID, 'otch')
        send_keys_with_delays(input_form_otch, otch,browser)
        browser.find_element(By.ID, 'bdate').send_keys(bdate)
        browser.find_element(By.ID, 'docno').send_keys(docno)
        browser.find_element(By.ID, 'docdt').send_keys(docdt)
        browser.find_element(By.ID, 'btn_send').click()
        time.sleep(2)
    except:
        print("Не найдено поле ввода!!!")

    try:
        result = browser.find_element(By.ID, 'resultInn')
        res = result.text
        if res == '':
            res ='Информация об ИНН не найдена.'

    except:
        print("Ненайдена информация ЦСС селектором на странице")
        res = "Ошибка"

    total_info = ['ФНС России, ИНН:', res,'Ссылка на ресурс:', browser.current_url,'Врем и дата запроса:', str(datetime.now())]
    print(total_info)
    return total_info
    browser.close()  # обяхательно закрываем сайт



