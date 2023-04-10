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

driver.get("https://www.google.com/")
rightcick=driver.find_element(By.XPATH,"//a[text()='Gmail']")
act=ActionChains(driver)
act.context_click(rightcick).perform()
