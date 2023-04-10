from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.google.com/")

driver.maximize_window()

title=driver.title
print(title)

driver.find_element(By.XPATH,"//title[text()='Google']")

driver.find_element(By.XPATH,"//img[@alt='Google' or @data-atf='1']")



link1=driver.find_element(By.XPATH,"//a[text()='தமிழ்']")
link1.click()
# link=driver.find_element(By.XPATH,"//a[text()='Gmail']")
# link.click()

Class=driver.find_element(By.XPATH,"//input[@class='gLFyf' or @type='tex']")
Class.send_keys("facebook")
link12=driver.find_element(By.XPATH,"//input[@class='RNmpXc']")
link12.click()
# driver.close()