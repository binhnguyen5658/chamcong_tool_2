# import necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# create a new instance of the Firefox driver
driver = webdriver.Firefox()
driver.implicitly_wait(10)

# navigate to the login page
driver.get("https://nncchamcongtool.streamlit.app")

try:
    element = driver.find_element(By.XPATH, '//button[contains(text(),"app back up")]')
except:
    print('still awake')
    pass
else:
    print('awake app')
    element.click()

sleep(10)

driver.close()



