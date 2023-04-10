import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

allink=driver.find_elements(By.XPATH,"//ul[@class='list']//descendant::a")   #no of elemnets mentioned
print(len(allink))
login=driver.find_element(By.LINK_TEXT,"Log in")
print(login.text)

for i in allink:
    sath=i.text
    print(sath)
