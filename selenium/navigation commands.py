import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.get("https://www.google.com/")
driver.get("https://www.google.com/")
driver.get("https://www.amazon.in/s?k=iphone&ref=nb_sb_noss")
driver.back()
time.sleep(3)
driver.back()
time.sleep(3)
driver.refresh()
driver.forward()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.quit()