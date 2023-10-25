# import necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from time import sleep

chromedriver_autoinstaller.install()

chrome_options = Options()
chrome_options.add_argument('--headless')

# create a new instance of the Chrome driver
driver = webdriver.Chrome(options=chrome_options)
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



