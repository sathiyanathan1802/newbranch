

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://www.google.com/")
inputbox=driver.find_element(By.NAME,"q")
# sa=inputbox.get_attribute("value")
# print(sa)



type=inputbox.get_attribute("autocomplete")
print(type)




