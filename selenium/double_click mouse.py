import time

import driver as driver
from _multiprocessing import send
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
field1=driver.find_element_by_id("field1")
field1.clear()
field1.send_keys("sathya")
field2=driver.find_element_by_id("field2")
copybutton=driver.find_element(By.XPATH,"//button[text()='Copy Text']")
act=ActionChains(driver)
act.double_click(copybutton).perform()
