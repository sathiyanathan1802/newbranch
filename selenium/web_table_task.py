import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
noofrow=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
row=len(noofrow)
noofcolumn=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
column=len(noofcolumn)

for r in range(2,row+1):
    price=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[4]").text
    if price=="300":
        bookname=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        author=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
        subject=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[3]").text
        print(bookname)

print()




