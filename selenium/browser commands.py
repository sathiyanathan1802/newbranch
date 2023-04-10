import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

link=driver.find_element(By.XPATH,"//a[text()='OrangeHRM, Inc']")
link.click()
time.sleep(5)

driver.get("https://www.facebook.com/")
time.sleep(3)
driver.quit()
