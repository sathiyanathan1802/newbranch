import time

from selenium import webdriver

from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

obj = webdriver.Chrome(ChromeDriverManager().install())

obj.get("https://itera-qa.azurewebsites.net/home/automation")

obj.maximize_window()

fname=obj.find_element(By.XPATH,"//input[@name='optionsRadios']")
fname.is_selected()
fname.click()
time.sleep(5)
obj.close()







