import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from auth_data import portal_password
from dates import date_2
import import_file



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

    # вводим логин на Портале
    login_input = driver.find_element(By.CSS_SELECTOR, 'input[type="text" i]')
    login_input.click()
    login_input.clear()
    login_input.send_keys("Pytsky_an")
    time.sleep(2)
    print("login OK")

    # вводим пароль на Портале
    password_input = driver.find_element(By.CSS_SELECTOR, 'input[type="password" i]')
    password_input.click()
    password_input.clear()
    password_input.send_keys(portal_password)
    time.sleep(2)
    print("password OK")

    # входим под логином и паролем на Портал
    login_button = driver.find_element(By.CSS_SELECTOR, 'button').click()
    time.sleep(5)
    print("auth OK")

    # жмем кнопку "Товародвижение аптек"
    report_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Товародвижение аптек')]").click()
    time.sleep(5)
    print("report_button OK")

    # устанавливаем галку "Не учитывать межскладскую передачу"
    special = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/form/div[4]/div[7]/label/div/span[1]')
    special.click()
    time.sleep(5)
    print("установил галку Не учитывать межскладскую передачу")

    # ищем путь до ввода значения начальной даты
    date_first_2 = driver.find_element(By.XPATH, '// *[ @ id = "react-select-2-input"]')

    # вводим значение даты из dates.py (переменная cell_2)
    date_first_2.send_keys(date_2)
    print("ввел начальную дату отчета")
    time.sleep(10)

    # жмем кнопку "Выгрузить в csv"
    generate = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/button[2]/span/span')
    generate.click()
    time.sleep(600)
    print("дождался формирования отчета")

    # скачиваем отчет
    bell = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div[1]/div/div/div[1]/div/div/div')
    bell.click()
    time.sleep(10)
    print("нажал колокольчик")

    download = driver.find_element(By.XPATH,  "//*[contains(text(), 'Скачать')]")
    download.click()
    time.sleep(300)
    print("скачал отчет")

    # закрываем загрузку
    bell = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div[1]/div/div/div[1]/div/div/div')
    bell.click()
    time.sleep(30)
    print("нажал колокольчик")

    close = driver.find_element(By.XPATH,  "//*[contains(text(), 'Закрыть')]")
    close.click()
    time.sleep(5)
    print("закрыл загрузку")

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

# вызываем функцию переименования и перемещения файла
import_file.import_last_file()

#123