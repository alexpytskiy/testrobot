import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from auth_data import portal_password


options = webdriver.ChromeOptions()

url = "https://portal.esc.ru/"
service = Service(executable_path = "L:\\ОТДЕЛЫ\ОТДЕЛ ФИЛИАЛОВ и ПРЕДСТАВИТЕЛЬСТВ\\Маркетинговый союз\\Отчёты\!Python projects\\test venv\\chromedriver\\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

try:
    driver.get(url=url)
    time.sleep(5)

    login_input = driver.find_element(By.CSS_SELECTOR, 'input[type="text" i]')
    login_input.click()
    login_input.clear()
    login_input.send_keys("Pytsky_an")
    time.sleep(2)
    print("login OK")

    password_input = driver.find_element(By.CSS_SELECTOR, 'input[type="password" i]')
    password_input.click()
    password_input.clear()
    password_input.send_keys(portal_password)
    time.sleep(2)
    print("password OK")

    login_button = driver.find_element(By.CSS_SELECTOR, 'button').click()
    time.sleep(5)
    print("auth OK")

    report_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Товародвижение аптек')]").click()
    time.sleep(5)
    print("report_button OK")

    date_first = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/form/div[3]/div[1]/div/div/div/div/div/div[1]')
    date_first.click()
    #date_first.clear()
    time.sleep(5)
    date_first.send_keys("20230101")
    time.sleep(15)

    date_second = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/form/div[3]/div[1]/div/div/div/div/div/div[2]')
    date_second.click()
    #date_second.clear()
    time.sleep(5)
    date_second.send_keys("20230101")
    time.sleep(15)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()