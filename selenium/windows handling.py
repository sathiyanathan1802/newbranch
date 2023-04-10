import time

import driver as driver
from _multiprocessing import send
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
input=driver.find_element(By.XPATH,"//input[@class='wikipedia-search-input']")
input.send_keys("selenium")
input.send_keys(Keys.ENTER)

alllinks=driver.find_elements(By.XPATH,"//div[@id='Wikipedia1_wikipedia-search-results']/descendant::a")
# alllinks =driver.find_elements(By.XPATH,"//div[@id='wikipedia-search-result-link']/a")   #list of webelement
for a in alllinks:
    a.click()

parentwindow=driver.current_window_handle
print(parentwindow)
allwindow=driver.window_handles
print(allwindow)

for handle in allwindow:
    driver.switch_to.window(handle)
    print(driver.title)

for window in allwindow:
    driver.switch_to.window(window)
    if driver.title=="Selenium disulfide - Wikipedia":
        all=driver.find_element(By.XPATH,"//input[@autocapitalize='sentences']")
        all.send_keys("selenium")
        time.sleep(3)
        # all.send_keys(Keys.ENTER)
        all1=driver.find_element(By.XPATH,"//button[@class='cdx-button cdx-button--action-default cdx-button--type-normal cdx-button--framed cdx-search-input__end-button']").click()


driver.quit()







