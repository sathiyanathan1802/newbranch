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
drag=driver.find_element(By.ID,"draggable")
drop=driver.find_element(By.ID,"droppable")
act=ActionChains(driver)
act.drag_and_drop(drag,drop).perform()
