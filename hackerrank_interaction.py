from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "L:\Development\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Abhilash")

lname = driver.find_element(By.NAME, "lName")
lname.send_keys("B J")

email = driver.find_element(By.NAME, "email")
email.send_keys("iambee@email.com")

button = driver.find_element(By.CLASS_NAME, "btn")
button.click()


# driver.get("https://www.hackerrank.com/")

# login = driver.find_element(By.LINK_TEXT, "Login")
# login.click()
#
# login_page = driver.find_element(By.CSS_SELECTOR, ".fl-button-width-auto a")
# login_page.click()
#
# username = driver.find_element(By.ID, "input-1")
# username.send_keys("")
# username.send_keys(Keys.ENTER)

# password = driver.find_element(By.ID, "input-2")
# password.send_keys("")
# # password.send_keys(Keys.TAB)
#
# login_button = driver.find_element(By.CSS_SELECTOR, ".align-icon-right span")
# print(login_button.text)
#
# driver.quit()
