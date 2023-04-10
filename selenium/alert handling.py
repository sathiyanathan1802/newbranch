import time

import driver as driver
import switch as switch
from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)


driver.get("https://the-internet.herokuapp.com/javascript_alerts")
button=driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']")
button.click()

alt=driver.switch_to.alert
alt.accept()

confirm_alert=driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']")
confirm_alert.click()
alt1=driver.switch_to.alert
alt1.accept()



a=driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']")
a.click()

alt2=driver.switch_to.alert
alt2.send_keys("sathyaagila")
alt2.accept()
