from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from random import choice

chrome_driver_path = "L:\Development\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
money = driver.find_element(By.ID, "money")

numbers = list(range(50))

while True:
    cookie.click()
    number = choice(numbers)
    if number == 0:
        stores = driver.find_elements(By.CSS_SELECTOR, "#store b")
        for store in reversed(stores):
            if store.text != "":
                amount = int(store.text.split()[-1].replace(",", ""))
                if int(money.text.replace(",", "")) > amount:
                    store.click()
                    break
