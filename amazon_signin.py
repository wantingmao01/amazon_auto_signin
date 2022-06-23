from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('DRIVER_PATH')

driver = webdriver.Chrome(service=s)
driver.get("https://www.amazon.com/")

# click sign in
driver.find_element(by = By.XPATH, value = '//a[@class="nav-a nav-a-2   nav-progressive-attribute"]').click()

# fill in email
driver.find_element(by = By.XPATH, value = "//input[@class = 'a-input-text a-span12 auth-autofocus auth-required-field']").send_keys("EMAIL or USER_NAME")

# click "continue" button
driver.find_element(by = By.XPATH, value = "//input[@class = 'a-button-input']").click()

# fill in password
driver.find_element(by = By.XPATH, value = "//input[@class = 'a-input-text a-span12 auth-autofocus auth-required-field']").send_keys("PASSWORD")

# click "sign-in" button
driver.find_element(by = By.XPATH, value = "//input[@class = 'a-button-input']").click()


