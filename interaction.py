from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "L:\Development\chromedriver.exe"
driver = webdriver.Chrome(service=Service(executable_path=chrome_driver_path))
driver.get("https://en.wikipedia.org/wiki/Main_Page")

count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(count.text)

driver.quit()
