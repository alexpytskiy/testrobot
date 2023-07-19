import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from auth_data import portal_password
from dates import date_2


options = webdriver.ChromeOptions()


url = "https://portal.esc.ru/"
service = Service(executable_path = "L:\\ОТДЕЛЫ\ОТДЕЛ ФИЛИАЛОВ и ПРЕДСТАВИТЕЛЬСТВ\\Маркетинговый союз\\Отчёты\!Python projects\\test venv\\chromedriver\\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

actions = ActionChains(driver)

try:
    driver.get(url=url)
    time.sleep(5)

    #вводим логин на Портале
    login_input = driver.find_element(By.CSS_SELECTOR, 'input[type="text" i]')
    login_input.click()
    login_input.clear()
    login_input.send_keys("Pytsky_an")
    time.sleep(2)
    print("login OK")

    #Вводим пароль на Портале
    password_input = driver.find_element(By.CSS_SELECTOR, 'input[type="password" i]')
    password_input.click()
    password_input.clear()
    password_input.send_keys(portal_password)
    time.sleep(2)
    print("password OK")

    #Входим под логином и паролем на Портал
    login_button = driver.find_element(By.CSS_SELECTOR, 'button').click()
    time.sleep(5)
    print("auth OK")

    #Жмем кнопку "Товародвижение аптек"
    report_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Товародвижение аптек')]").click()
    time.sleep(5)
    print("report_button OK")

    #Выбираем начальную дату в календаре
    #date_first = driver.find_element(By.XPATH, "//div[@class='css-s1rjxz']")
    #date_first.click()
    #time.sleep(5)
    #print("выбрал календарик")

    #ищем путь до ввода значения начальной даты
    date_first_2 = driver.find_element(By.XPATH, '// *[ @ id = "react-select-2-input"]')

    #вводим значение даты из dates.py (переменная cell_2)
    date_first_2.send_keys(date_2)

    print("ввел начальную дату отчета")
    time.sleep(10)

    # date_first_exit = driver.find_element(By.XPATH, '// *[ @ id = "react-select-2-input"]')
    # date_first_exit.click()
    # time.sleep(5)
    # print("убрал календарик")
    #
    # special = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/form/div[4]/div[7]/label/div/span[1]/span/svg/g/path')
    # special.click()
    # print("установил галку не учитывать межскладскую передачу")
    # time.sleep(10)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()