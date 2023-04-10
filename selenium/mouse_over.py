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

driver.get("https://www.amazon.in/s?k=iphone&ref=nb_sb_noss")
mouseover=driver.find_element(By.XPATH,"//div[@class='nav-line-1-container']//following-sibling::span/span")
act=ActionChains(driver)
act.move_to_element(mouseover).perform()
click=driver.find_element(By.XPATH,"//span[text()='Your Wish List']").click()

