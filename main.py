from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "L:\Development\chromedriver.exe"
driver = webdriver.Chrome(service=Service(executable_path=chrome_driver_path))
driver.get("https://www.python.org/")


times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
links = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
menu = {}
for index, (time, link) in enumerate(zip(times, links)):
    menu[index] = {"time": time.get_attribute("datetime").split("T")[0],
                   "name": link.text}

print(menu)

driver.quit()
